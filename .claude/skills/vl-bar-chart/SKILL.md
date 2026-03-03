---
name: vl-bar-chart
description: Vega-Lite v5 reference and examples for bar charts (mark bar).
---

# Vega-Lite Bar Chart

## Minimal example

```json
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {"url": "https://vega.github.io/vega-datasets/data/seattle-weather.csv"},
  "mark": "bar",
  "encoding": {
    "x": {"field": "weather", "type": "nominal"},
    "y": {"aggregate": "count", "type": "quantitative"}
  }
}
```

## Grouped bar chart

```json
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {"url": "https://vega.github.io/vega-datasets/data/seattle-weather.csv"},
  "mark": "bar",
  "encoding": {
    "x": {"field": "weather", "type": "nominal"},
    "y": {"aggregate": "count", "type": "quantitative"},
    "color": {"field": "weather", "type": "nominal"},
    "xOffset": {"field": "weather", "type": "nominal"}
  }
}
```

## Horizontal bar chart

Swap x/y and use `nominal` on y:

```json
{
  "mark": "bar",
  "encoding": {
    "y": {"field": "Category", "type": "nominal", "sort": "-x"},
    "x": {"field": "Value", "type": "quantitative"}
  }
}
```

## Stacked bar chart

Use `color` encoding — Vega-Lite stacks automatically:

```json
{
  "mark": "bar",
  "encoding": {
    "x": {"field": "Year", "type": "ordinal"},
    "y": {"field": "Sales", "type": "quantitative"},
    "color": {"field": "Category", "type": "nominal"}
  }
}
```

## Key options

| Property | Values | Notes |
|----------|--------|-------|
| `mark.cornerRadius` | number | Rounds bar corners |
| `mark.width` | number | Fixed bar width in pixels |
| `encoding.y.stack` | `"normalize"` | 100% stacked bars |
| `encoding.y.sort` | `"-x"` / `"x"` | Sort by value |
