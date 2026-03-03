---
name: vl-aggregation
description: Vega-Lite v5 aggregation functions reference — sum, mean, count, min, max, and more.
---

# Vega-Lite Aggregation

Vega-Lite can aggregate data within the visualization spec. Use the `aggregate` property on an encoding channel.

## All aggregation functions

| Function | Description | Input type |
|----------|-------------|------------|
| `count` | Number of records | any |
| `valid` | Non-null record count | any |
| `missing` | Null record count | any |
| `distinct` | Distinct value count | any |
| `sum` | Sum of values | numeric |
| `mean` | Arithmetic mean | numeric |
| `average` | Alias for mean | numeric |
| `median` | Median value | numeric |
| `min` | Minimum value | numeric / temporal |
| `max` | Maximum value | numeric / temporal |
| `variance` | Variance | numeric |
| `variancep` | Population variance | numeric |
| `stdev` | Standard deviation | numeric |
| `stdevp` | Population std dev | numeric |
| `stderr` | Standard error | numeric |
| `q1` | Lower quartile (25th) | numeric |
| `q3` | Upper quartile (75th) | numeric |
| `ci0` | Lower confidence interval | numeric |
| `ci1` | Upper confidence interval | numeric |
| `product` | Product of all values | numeric |
| `argmin` | Row with min value | any |
| `argmax` | Row with max value | any |

## Usage

```json
"encoding": {
  "x": {"field": "Origin", "type": "nominal"},
  "y": {"field": "Miles_per_Gallon", "type": "quantitative", "aggregate": "mean"}
}
```

## Count (no field needed)

```json
"y": {"aggregate": "count", "type": "quantitative"}
```

No `field` is needed for `count`.

## Binning (histograms)

```json
"x": {"field": "Horsepower", "type": "quantitative", "bin": true},
"y": {"aggregate": "count", "type": "quantitative"}
```

Fine-tune with `bin` object:

```json
"bin": {"maxbins": 20}
"bin": {"step": 10}
"bin": {"extent": [0, 300]}
```

## Transform-based aggregation

For complex aggregations (multiple outputs), use `transform`:

```json
"transform": [
  {
    "aggregate": [
      {"op": "mean", "field": "Sales", "as": "mean_sales"},
      {"op": "stdev", "field": "Sales", "as": "stdev_sales"}
    ],
    "groupby": ["Category", "Year"]
  }
]
```

## Error bars with aggregation

```json
{
  "mark": "errorbar",
  "encoding": {
    "x": {"field": "variety", "type": "nominal"},
    "y": {"field": "yield", "type": "quantitative", "aggregate": "mean"},
    "yError": {"field": "yield", "aggregate": "stdev"}
  }
}
```
