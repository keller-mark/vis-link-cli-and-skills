---
name: connect
description: Save a vis-link session ID so subsequent CLI commands know which browser session to target.
---

# connect

Save a session ID from the browser to your local machine (`~/.vislink/session`).

## Usage

```
vislink connect SESSION_ID
```

The session ID is displayed in the browser when you open `http://localhost:8000`.

## Workflow

1. Start the server: `uv run uvicorn server:app --reload`
2. Open `http://localhost:8000` in a browser — the session ID appears at the top.
3. Copy the session ID and run:

```bash
vislink connect 3f2a1b4c-...
```

4. All subsequent commands (`get-spec`, `set-mark`, etc.) will use that session automatically.

## Notes

- The session ID is a UUID generated fresh each time the browser connects.
- Refreshing the browser creates a new session; you will need to run `connect` again.
- The saved session is stored in `~/.vislink/session` as plain text.
