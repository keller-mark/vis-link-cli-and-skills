---
name: vl-scatter
description: Vega-Lite v5 reference and examples for scatter plots (mark point).
---

# Vega-Lite Scatter Plot

## Minimal example

```json
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {"url": "https://vega.github.io/vega-datasets/data/cars.json"},
  "mark": {"type": "point", "tooltip": true},
  "encoding": {
    "x": {"field": "Horsepower", "type": "quantitative"},
    "y": {"field": "Miles_per_Gallon", "type": "quantitative"}
  }
}
```

## With color and size

```json
{
  "mark": {"type": "point", "tooltip": true},
  "encoding": {
    "x": {"field": "Horsepower", "type": "quantitative"},
    "y": {"field": "Miles_per_Gallon", "type": "quantitative"},
    "color": {"field": "Origin", "type": "nominal"},
    "size": {"field": "Acceleration", "type": "quantitative"}
  }
}
```

## With regression line overlay

Use a layer spec:

```json
{
  "layer": [
    {
      "mark": "point",
      "encoding": {
        "x": {"field": "Horsepower", "type": "quantitative"},
        "y": {"field": "Miles_per_Gallon", "type": "quantitative"}
      }
    },
    {
      "mark": {"type": "line", "color": "firebrick"},
      "transform": [{"regression": "Miles_per_Gallon", "on": "Horsepower"}],
      "encoding": {
        "x": {"field": "Horsepower", "type": "quantitative"},
        "y": {"field": "Miles_per_Gallon", "type": "quantitative"}
      }
    }
  ]
}
```

## Key options

| Property | Values | Notes |
|----------|--------|-------|
| `mark.filled` | `true` | Filled circles |
| `mark.opacity` | 0–1 | Transparency for overplotting |
| `mark.shape` | `"circle"`, `"square"`, `"cross"`, etc. | Point shape |
| `mark.size` | number | Fixed point size in pixels² |
| `encoding.shape` | field encoding | Vary shape by category |
