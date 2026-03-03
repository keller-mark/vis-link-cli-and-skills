---
name: vl-area-chart
description: Vega-Lite v5 reference and examples for area charts (mark area).
---

# Vega-Lite Area Chart

## Minimal example

```json
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {"url": "https://vega.github.io/vega-datasets/data/seattle-weather.csv"},
  "mark": "area",
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "temp_max", "type": "quantitative"}
  }
}
```

## Stacked area chart

```json
{
  "mark": "area",
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "count", "type": "quantitative"},
    "color": {"field": "category", "type": "nominal"}
  }
}
```

## Streamgraph (normalized stacked area)

```json
{
  "mark": "area",
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "count", "type": "quantitative", "stack": "center", "axis": null},
    "color": {"field": "category", "type": "nominal"}
  }
}
```

## Area with line overlay

```json
{
  "mark": {"type": "area", "line": true, "opacity": 0.3}
}
```

## Gradient area (single color)

```json
{
  "mark": {
    "type": "area",
    "line": {"color": "darkgreen"},
    "color": {
      "x1": 1, "y1": 1, "x2": 1, "y2": 0,
      "gradient": "linear",
      "stops": [
        {"offset": 0, "color": "white"},
        {"offset": 1, "color": "darkgreen"}
      ]
    }
  }
}
```

## Key options

| Property | Values | Notes |
|----------|--------|-------|
| `mark.line` | `true` / object | Add border line on top |
| `mark.opacity` | 0–1 | Fill opacity |
| `mark.interpolate` | `"monotone"`, `"step"` | Smoothing |
| `encoding.y.stack` | `"normalize"`, `"center"` | 100% or streamgraph |
