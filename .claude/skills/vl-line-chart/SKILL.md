---
name: vl-line-chart
description: Vega-Lite v5 reference and examples for line charts (mark line).
---

# Vega-Lite Line Chart

## Minimal example

```json
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {"url": "https://vega.github.io/vega-datasets/data/seattle-weather.csv"},
  "mark": "line",
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "temp_max", "type": "quantitative"}
  }
}
```

## Multi-series line chart

```json
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {"url": "https://vega.github.io/vega-datasets/data/stocks.csv"},
  "mark": "line",
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "price", "type": "quantitative"},
    "color": {"field": "symbol", "type": "nominal"}
  }
}
```

## Line with points overlay

```json
{
  "mark": {"type": "line", "point": true}
}
```

## Smoothed line (monotone interpolation)

```json
{
  "mark": {"type": "line", "interpolate": "monotone"}
}
```

## Aggregated line

```json
{
  "mark": "line",
  "encoding": {
    "x": {"field": "Year", "type": "ordinal"},
    "y": {"field": "Sales", "type": "quantitative", "aggregate": "mean"}
  }
}
```

## Key options

| Property | Values | Notes |
|----------|--------|-------|
| `mark.interpolate` | `"linear"`, `"monotone"`, `"step"`, `"cardinal"` | Line smoothing |
| `mark.point` | `true` / object | Overlay point marks |
| `mark.strokeDash` | `[4, 4]` | Dashed line |
| `mark.strokeWidth` | number | Line thickness |
