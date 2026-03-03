---
name: vl-marks
description: Complete Vega-Lite v5 mark type reference with key properties for each mark.
---

# Vega-Lite Marks Reference

## Mark shorthand vs object

```json
"mark": "bar"
// or with options:
"mark": {"type": "bar", "cornerRadius": 4, "tooltip": true}
```

## All mark types

| Mark | Best for | Key channels |
|------|----------|-------------|
| `point` | Scatter plots, dot plots | x, y, color, size, shape, opacity |
| `bar` | Bar/column charts, histograms | x, y, color, xOffset |
| `line` | Time series, trends | x, y, color, strokeDash |
| `area` | Area charts, streamgraphs | x, y, color |
| `rect` | Heatmaps, 2D histograms | x, y, x2, y2, color |
| `arc` | Pie charts, donut charts | theta, color, radius |
| `text` | Labels, annotations | x, y, text, color |
| `tick` | Strip plots, dot plots | x, y, color |
| `rule` | Reference lines, error bars | x, y, x2, y2, color |
| `boxplot` | Distribution summaries | x, y, color |
| `errorband` | Confidence intervals | x, y, color |
| `errorbar` | Error bars | x, y, color |
| `geoshape` | Choropleth maps | color |
| `image` | Image overlays | url, x, y |
| `trail` | Variable-width lines | x, y, size, color |

## Common mark properties

| Property | Type | Description |
|----------|------|-------------|
| `tooltip` | bool/object | Show tooltip on hover |
| `opacity` | 0–1 | Overall opacity |
| `color` | string | Fixed color (overridden by encoding) |
| `filled` | bool | Fill vs stroke for point/arc |
| `size` | number | Size in px² (point) or px (bar width) |
| `strokeWidth` | number | Border line width |
| `cornerRadius` | number | Rounded corners (bar, rect) |
| `cursor` | string | CSS cursor on hover |
| `clip` | bool | Clip mark to plot area |

## Arc (pie/donut) example

```json
{
  "mark": {"type": "arc", "innerRadius": 50},
  "encoding": {
    "theta": {"field": "value", "type": "quantitative"},
    "color": {"field": "category", "type": "nominal"}
  }
}
```

## Boxplot example

```json
{
  "mark": {"type": "boxplot", "extent": "min-max"},
  "encoding": {
    "x": {"field": "Origin", "type": "nominal"},
    "y": {"field": "Miles_per_Gallon", "type": "quantitative"}
  }
}
```
