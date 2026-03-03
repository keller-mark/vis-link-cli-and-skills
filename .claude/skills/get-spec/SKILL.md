---
name: get-spec
description: Retrieve and print the current Vega-Lite spec from the live browser session as JSON.
---

# get-spec

Fetch the canonical Vega-Lite spec currently held by the server for the active session.

## Usage

```
vislink get-spec
```

Prints the spec as pretty-printed JSON to stdout.

## Example

```bash
vislink get-spec
```

Output:

```json
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": { "url": "https://vega.github.io/vega-datasets/data/cars.json" },
  "mark": { "type": "point", "tooltip": true },
  "encoding": {
    "x": { "field": "Horsepower", "type": "quantitative" },
    "y": { "field": "Miles_per_Gallon", "type": "quantitative" },
    "color": { "field": "Origin", "type": "nominal" }
  }
}
```

## Notes

- The server holds the canonical spec; no browser round-trip is needed.
- Use the output as input to `set-spec` after modifying it.
- Requires a saved session (run `vislink connect SESSION_ID` first).
