---
name: vl-heatmap
description: Vega-Lite v5 reference and examples for heatmaps (mark rect).
---

# Vega-Lite Heatmap

## Minimal example

```json
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {"url": "https://vega.github.io/vega-datasets/data/seattle-weather.csv"},
  "mark": "rect",
  "encoding": {
    "x": {"field": "date", "type": "ordinal", "timeUnit": "date", "title": "Day"},
    "y": {"field": "date", "type": "ordinal", "timeUnit": "month", "title": "Month"},
    "color": {"field": "temp_max", "type": "quantitative", "aggregate": "mean", "title": "Avg Max Temp"}
  }
}
```

## 2D categorical heatmap

```json
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {"url": "https://vega.github.io/vega-datasets/data/cars.json"},
  "mark": "rect",
  "encoding": {
    "x": {"field": "Cylinders", "type": "ordinal"},
    "y": {"field": "Origin", "type": "nominal"},
    "color": {"field": "Horsepower", "type": "quantitative", "aggregate": "mean"}
  }
}
```

## With text labels overlay

```json
{
  "layer": [
    {
      "mark": "rect",
      "encoding": {
        "x": {"field": "col", "type": "ordinal"},
        "y": {"field": "row", "type": "ordinal"},
        "color": {"field": "value", "type": "quantitative"}
      }
    },
    {
      "mark": "text",
      "encoding": {
        "x": {"field": "col", "type": "ordinal"},
        "y": {"field": "row", "type": "ordinal"},
        "text": {"field": "value", "type": "quantitative", "format": ".1f"},
        "color": {"condition": {"test": "datum.value > 50", "value": "white"}, "value": "black"}
      }
    }
  ]
}
```

## Color schemes

```json
"color": {
  "field": "value",
  "type": "quantitative",
  "scale": {"scheme": "viridis"}
}
```

Common schemes: `"blues"`, `"reds"`, `"viridis"`, `"plasma"`, `"redblue"` (diverging).

## Key options

| Property | Values | Notes |
|----------|--------|-------|
| `mark.width` | number | Fixed cell width |
| `mark.height` | number | Fixed cell height |
| `encoding.color.scale.scheme` | string | Color palette |
| `encoding.color.scale.domain` | `[min, max]` | Fix color range |
