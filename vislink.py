"""vislink CLI — WebSocket client for the vis-link server."""
import argparse
import asyncio
import json
import sys
from pathlib import Path

import websockets

SESSION_FILE = Path.home() / ".vislink" / "session"
DEFAULT_WS_URL = "ws://localhost:8000/ws/cli"

VALID_MARKS = ["point", "bar", "line", "area", "rect", "arc", "text", "tick", "rule"]


def load_session() -> str:
    if not SESSION_FILE.exists():
        print("No session saved. Run: vislink connect SESSION_ID", file=sys.stderr)
        sys.exit(1)
    return SESSION_FILE.read_text().strip()


def save_session(session_id: str) -> None:
    SESSION_FILE.parent.mkdir(parents=True, exist_ok=True)
    SESSION_FILE.write_text(session_id)


async def _connect_and_run(session_id: str, messages: list[dict], ws_url: str = DEFAULT_WS_URL) -> list[dict]:
    """Open one CLI WebSocket, authenticate, send messages, collect responses, close."""
    responses = []
    async with websockets.connect(ws_url) as ws:
        await ws.send(json.dumps({"type": "connect", "session_id": session_id}))
        ack = json.loads(await ws.recv())
        if ack.get("type") == "error":
            print(f"Error: {ack['message']}", file=sys.stderr)
            sys.exit(1)

        for msg in messages:
            await ws.send(json.dumps(msg))
            resp = json.loads(await ws.recv())
            responses.append(resp)
            if resp.get("type") == "error":
                print(f"Error: {resp['message']}", file=sys.stderr)
                sys.exit(1)

    return responses


def cmd_connect(args: argparse.Namespace) -> None:
    session_id = args.session_id.strip()
    save_session(session_id)
    print(f"Session saved: {session_id}")


def cmd_get_spec(args: argparse.Namespace) -> None:
    session_id = load_session()
    responses = asyncio.run(_connect_and_run(session_id, [{"type": "get_spec"}]))
    spec = responses[0].get("spec")
    print(json.dumps(spec, indent=2))


def cmd_set_spec(args: argparse.Namespace) -> None:
    session_id = load_session()

    if args.file:
        spec = json.loads(Path(args.file).read_text())
    else:
        spec = json.loads(args.spec)

    asyncio.run(_connect_and_run(session_id, [{"type": "set_spec", "spec": spec}]))
    print("Spec updated.")


def cmd_set_mark(args: argparse.Namespace) -> None:
    session_id = load_session()

    # get current spec, modify mark, set it back — all in one connection
    async def run() -> None:
        async with websockets.connect(DEFAULT_WS_URL) as ws:
            await ws.send(json.dumps({"type": "connect", "session_id": session_id}))
            ack = json.loads(await ws.recv())
            if ack.get("type") == "error":
                print(f"Error: {ack['message']}", file=sys.stderr)
                sys.exit(1)

            await ws.send(json.dumps({"type": "get_spec"}))
            resp = json.loads(await ws.recv())
            spec = resp["spec"]

            # Update mark (preserve existing mark options, just change type)
            mark = spec.get("mark", {})
            if isinstance(mark, str):
                mark = {"type": mark}
            mark["type"] = args.mark
            spec["mark"] = mark

            await ws.send(json.dumps({"type": "set_spec", "spec": spec}))
            resp = json.loads(await ws.recv())
            if resp.get("type") == "error":
                print(f"Error: {resp['message']}", file=sys.stderr)
                sys.exit(1)

    asyncio.run(run())
    print(f"Mark set to: {args.mark}")


def cmd_set_encoding(args: argparse.Namespace) -> None:
    session_id = load_session()

    async def run() -> None:
        async with websockets.connect(DEFAULT_WS_URL) as ws:
            await ws.send(json.dumps({"type": "connect", "session_id": session_id}))
            ack = json.loads(await ws.recv())
            if ack.get("type") == "error":
                print(f"Error: {ack['message']}", file=sys.stderr)
                sys.exit(1)

            await ws.send(json.dumps({"type": "get_spec"}))
            resp = json.loads(await ws.recv())
            spec = resp["spec"]

            encoding_def: dict = {"field": args.field, "type": args.type}
            if args.aggregate:
                encoding_def["aggregate"] = args.aggregate
            if args.title:
                encoding_def["title"] = args.title

            if "encoding" not in spec:
                spec["encoding"] = {}
            spec["encoding"][args.channel] = encoding_def

            await ws.send(json.dumps({"type": "set_spec", "spec": spec}))
            resp = json.loads(await ws.recv())
            if resp.get("type") == "error":
                print(f"Error: {resp['message']}", file=sys.stderr)
                sys.exit(1)

    asyncio.run(run())
    print(f"Encoding {args.channel} set to field '{args.field}' ({args.type})")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="vislink",
        description="Control a live Vega-Lite visualization over WebSocket",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # connect
    p_connect = subparsers.add_parser("connect", help="Save a session ID for subsequent commands")
    p_connect.add_argument("session_id", help="Session ID displayed in the browser")
    p_connect.set_defaults(func=cmd_connect)

    # get-spec
    p_get = subparsers.add_parser("get-spec", help="Print the current Vega-Lite spec as JSON")
    p_get.set_defaults(func=cmd_get_spec)

    # set-spec
    p_set = subparsers.add_parser("set-spec", help="Replace the current Vega-Lite spec")
    spec_group = p_set.add_mutually_exclusive_group(required=True)
    spec_group.add_argument("--file", metavar="PATH", help="Path to a JSON spec file")
    spec_group.add_argument("--spec", metavar="JSON", help="Spec as a JSON string")
    p_set.set_defaults(func=cmd_set_spec)

    # set-mark
    p_mark = subparsers.add_parser("set-mark", help="Change the mark type of the current spec")
    p_mark.add_argument("mark", choices=VALID_MARKS, help="Vega-Lite mark type")
    p_mark.set_defaults(func=cmd_set_mark)

    # set-encoding
    p_enc = subparsers.add_parser("set-encoding", help="Set or replace an encoding channel")
    p_enc.add_argument("channel", help="Encoding channel (e.g. x, y, color, size)")
    p_enc.add_argument("field", help="Data field name")
    p_enc.add_argument(
        "--type",
        default="quantitative",
        choices=["quantitative", "nominal", "ordinal", "temporal"],
        help="Field type (default: quantitative)",
    )
    p_enc.add_argument("--aggregate", help="Aggregation function (e.g. mean, sum, count)")
    p_enc.add_argument("--title", help="Axis/legend title")
    p_enc.set_defaults(func=cmd_set_encoding)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
