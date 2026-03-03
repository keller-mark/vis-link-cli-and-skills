import uuid
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.templating import Jinja2Templates
from starlette.websockets import WebSocket, WebSocketDisconnect

DEFAULT_SPEC = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "description": "A scatter plot of the cars dataset.",
    "data": {"url": "https://vega.github.io/vega-datasets/data/cars.json"},
    "mark": {"type": "point", "tooltip": True},
    "encoding": {
        "x": {"field": "Horsepower", "type": "quantitative"},
        "y": {"field": "Miles_per_Gallon", "type": "quantitative"},
        "color": {"field": "Origin", "type": "nominal"},
    },
}

# session_id -> {"frontend": WebSocket | None, "spec": dict}
sessions: dict[str, dict] = {}

templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


async def homepage(request: Request) -> HTMLResponse:
    scheme = "wss" if request.url.scheme == "https" else "ws"
    ws_url = f"{scheme}://{request.url.netloc}/ws/frontend"
    return templates.TemplateResponse(request, "index.html", {"ws_url": ws_url})


async def frontend_websocket(ws: WebSocket) -> None:
    await ws.accept()
    session_id = str(uuid.uuid4())
    sessions[session_id] = {"frontend": ws, "spec": dict(DEFAULT_SPEC)}

    try:
        await ws.send_json({"type": "session_id", "session_id": session_id})
        await ws.send_json({"type": "set_spec", "spec": sessions[session_id]["spec"]})

        # Keep connection alive; browser doesn't send messages but we need to detect close
        while True:
            await ws.receive_text()
    except WebSocketDisconnect:
        pass
    finally:
        if session_id in sessions:
            sessions[session_id]["frontend"] = None


async def cli_websocket(ws: WebSocket) -> None:
    await ws.accept()

    try:
        # First message must be a connect with a valid session_id
        msg = await ws.receive_json()
        if msg.get("type") != "connect":
            await ws.send_json({"type": "error", "message": "First message must be {type: connect, session_id: ...}"})
            await ws.close()
            return

        session_id = msg.get("session_id")
        if session_id not in sessions:
            await ws.send_json({"type": "error", "message": f"Unknown session_id: {session_id}"})
            await ws.close()
            return

        await ws.send_json({"type": "ack", "session_id": session_id})

        # Handle command messages
        while True:
            cmd = await ws.receive_json()
            cmd_type = cmd.get("type")

            if cmd_type == "get_spec":
                await ws.send_json({"type": "spec", "spec": sessions[session_id]["spec"]})

            elif cmd_type == "set_spec":
                spec = cmd.get("spec")
                if spec is None:
                    await ws.send_json({"type": "error", "message": "set_spec requires a spec field"})
                    continue
                sessions[session_id]["spec"] = spec
                frontend = sessions[session_id].get("frontend")
                if frontend is not None:
                    try:
                        await frontend.send_json({"type": "set_spec", "spec": spec})
                    except Exception:
                        sessions[session_id]["frontend"] = None
                await ws.send_json({"type": "ack", "message": "spec updated"})

            else:
                await ws.send_json({"type": "error", "message": f"Unknown command type: {cmd_type}"})

    except WebSocketDisconnect:
        pass


app = Starlette(
    routes=[
        Route("/", homepage),
        WebSocketRoute("/ws/frontend", frontend_websocket),
        WebSocketRoute("/ws/cli", cli_websocket),
    ]
)
