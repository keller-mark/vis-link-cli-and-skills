---
name: vl-encodings
description: Vega-Lite v5 encoding channels reference — positional, color, size, shape, text, and more.
---

# Vega-Lite Encodings Reference

## Encoding channel categories

### Positional
| Channel | Description |
|---------|-------------|
| `x` | Horizontal position |
| `y` | Vertical position |
| `x2` | Second x (for rect/rule spans) |
| `y2` | Second y |
| `xOffset` | Offset within band (grouped bars) |
| `yOffset` | Offset within band |
| `longitude` | Geo longitude |
| `latitude` | Geo latitude |

### Color / Opacity
| Channel | Description |
|---------|-------------|
| `color` | Fill/stroke color |
| `fill` | Fill color (overrides color) |
| `stroke` | Stroke color |
| `opacity` | Overall opacity |
| `fillOpacity` | Fill opacity only |
| `strokeOpacity` | Stroke opacity only |

### Size / Shape
| Channel | Description |
|---------|-------------|
| `size` | Mark size (area in px² for points) |
| `shape` | Point shape symbol |
| `strokeWidth` | Stroke width |
| `strokeDash` | Dash pattern |

### Text / Tooltip
| Channel | Description |
|---------|-------------|
| `text` | Text label content |
| `tooltip` | Tooltip content |

### Order / Detail
| Channel | Description |
|---------|-------------|
| `order` | Drawing order / sort order in stacks |
| `detail` | Group without visual encoding |
| `facet` | Facet (small multiples) |
| `row` | Facet rows |
| `column` | Facet columns |

## Encoding definition properties

```json
"encoding": {
  "x": {
    "field": "FieldName",       // data field
    "type": "quantitative",     // field type
    "aggregate": "mean",        // aggregation
    "bin": true,                // binning
    "timeUnit": "year",         // time unit
    "title": "Axis Title",      // axis/legend label
    "scale": {"zero": false},   // scale config
    "axis": {"grid": false},    // axis config
    "sort": "ascending",        // sort order
    "stack": "normalize"        // stacking mode
  }
}
```

## Condition (if/else encoding)

```json
"color": {
  "condition": {"test": "datum.value > 100", "value": "red"},
  "value": "steelblue"
}
```

## Shorthand string syntax

```json
"x": "Horsepower:Q"      // quantitative
"y": "date:T"            // temporal
"color": "Origin:N"      // nominal
"shape": "Cylinders:O"   // ordinal
```

Type abbreviations: `Q` = quantitative, `N` = nominal, `O` = ordinal, `T` = temporal, `G` = geojson.
