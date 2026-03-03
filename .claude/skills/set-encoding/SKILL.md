---
name: set-encoding
description: Set or replace a single Vega-Lite encoding channel (x, y, color, size, etc.) without replacing the whole spec.
---

# set-encoding

Update one encoding channel of the current spec. Other channels and the mark are unchanged.

## Usage

```
vislink set-encoding CHANNEL FIELD [--type TYPE] [--aggregate AGG] [--title TITLE]
```

## Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `CHANNEL` | yes | Encoding channel: `x`, `y`, `color`, `size`, `shape`, `opacity`, `tooltip`, etc. |
| `FIELD` | yes | Name of the data field |
| `--type` | no | Field type: `quantitative`, `nominal`, `ordinal`, `temporal` (default: `quantitative`) |
| `--aggregate` | no | Aggregation: `mean`, `sum`, `count`, `min`, `max`, `median`, etc. |
| `--title` | no | Axis or legend title |

## Examples

```bash
# Set x to a nominal field
vislink set-encoding x Name --type nominal

# Set y to mean of Miles_per_Gallon
vislink set-encoding y Miles_per_Gallon --aggregate mean --title "Avg MPG"

# Set color to a temporal field
vislink set-encoding color Year --type temporal

# Set size to a quantitative field
vislink set-encoding size Acceleration --type quantitative
```

## Notes

- Uses get→modify→set in a single WebSocket connection.
- Replaces the entire definition for that channel; any previous shorthand is overwritten.
- Requires a saved session (run `vislink connect SESSION_ID` first).
