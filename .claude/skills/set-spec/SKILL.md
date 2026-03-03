---
name: set-spec
description: Replace the current Vega-Lite spec in the live browser session with a new one from a file or JSON string.
---

# set-spec

Push a complete Vega-Lite spec to the server, which immediately updates the browser visualization.

## Usage

```
vislink set-spec --file PATH
vislink set-spec --spec JSON_STRING
```

`--file` and `--spec` are mutually exclusive; one is required.

## Examples

**From a file:**

```bash
vislink set-spec --file my_chart.json
```

**From a JSON string:**

```bash
vislink set-spec --spec '{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {"url": "https://vega.github.io/vega-datasets/data/seattle-weather.csv"},
  "mark": "bar",
  "encoding": {
    "x": {"field": "weather", "type": "nominal"},
    "y": {"aggregate": "count", "type": "quantitative"},
    "color": {"field": "weather", "type": "nominal"}
  }
}'
```

**Agent workflow — modify then push:**

```bash
# 1. Get the current spec
vislink get-spec > /tmp/spec.json

# 2. Edit /tmp/spec.json (or have the agent edit it)

# 3. Push updated spec
vislink set-spec --file /tmp/spec.json
```

## Notes

- The spec must be valid Vega-Lite v5 JSON.
- The server broadcasts the new spec to all connected browser frontends for that session.
- For targeted edits (mark type, single encoding), prefer `set-mark` and `set-encoding` instead.
