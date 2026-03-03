---
name: set-mark
description: Change the mark type of the current Vega-Lite spec without replacing the whole spec.
---

# set-mark

Change only the `mark.type` of the current spec. All other mark properties and encodings are preserved.

## Usage

```
vislink set-mark MARK
```

## Valid mark types

| Mark | Description |
|------|-------------|
| `point` | Scatter plot dots |
| `bar` | Bar chart rectangles |
| `line` | Connected line |
| `area` | Filled area under a line |
| `rect` | Filled rectangles (heatmaps) |
| `arc` | Pie/donut slices |
| `text` | Text labels |
| `tick` | Strip plot ticks |
| `rule` | Reference lines |

## Examples

```bash
# Switch to bar chart
vislink set-mark bar

# Switch back to scatter
vislink set-mark point

# Switch to line chart
vislink set-mark line
```

## How it works

`set-mark` opens one WebSocket connection, fetches the current spec with `get_spec`, updates `mark.type`, and pushes the result with `set_spec` — all atomically in a single connection.

## Notes

- Existing mark options (e.g. `tooltip: true`, `filled: true`) are preserved.
- If the current spec uses a string mark (e.g. `"mark": "bar"`), it is promoted to an object before updating.
- Requires a saved session (run `vislink connect SESSION_ID` first).
