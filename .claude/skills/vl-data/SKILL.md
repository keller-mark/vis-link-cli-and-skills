---
name: vl-data
description: Vega-Lite v5 data source reference — URL, inline values, named datasets, and transforms.
---

# Vega-Lite Data Reference

## Data source types

### URL

```json
"data": {"url": "https://vega.github.io/vega-datasets/data/cars.json"}
```

Supported formats: `.json`, `.csv`, `.tsv`, `.dsv`.

Specify format explicitly if needed:

```json
"data": {
  "url": "data/flights.csv",
  "format": {"type": "csv", "parse": {"date": "date", "delay": "number"}}
}
```

### Inline values (JSON array)

```json
"data": {
  "values": [
    {"category": "A", "value": 10},
    {"category": "B", "value": 20},
    {"category": "C", "value": 15}
  ]
}
```

### Named dataset (Vega datasets)

Available via the `vega-datasets` CDN:

```
https://vega.github.io/vega-datasets/data/DATASET
```

| Dataset | Description |
|---------|-------------|
| `cars.json` | Car specs: Horsepower, MPG, Origin, Year |
| `seattle-weather.csv` | Daily weather: date, temp, precip, weather |
| `stocks.csv` | Stock prices: symbol, date, price |
| `unemployment-across-industries.json` | Monthly unemployment by sector |
| `iris.json` | Iris flower measurements (classification) |
| `movies.json` | Movie ratings: IMDB, Rotten Tomatoes |
| `flights-5k.json` | 5k flight records: delay, distance, origin |
| `population.json` | US population by year and age |
| `us-10m.json` | US TopoJSON for choropleth maps |
| `world-110m.json` | World TopoJSON |

### Graticule (geo grid lines)

```json
"data": {"graticule": true}
```

### Sphere (world outline)

```json
"data": {"sphere": true}
```

## Data transforms

Apply inline transformations before encoding:

```json
"transform": [
  {"filter": "datum.Horsepower > 100"},
  {"calculate": "datum.Miles_per_Gallon * 0.425", "as": "km_per_liter"},
  {"aggregate": [{"op": "mean", "field": "km_per_liter", "as": "mean_kml"}], "groupby": ["Origin"]},
  {"sort": [{"field": "mean_kml", "order": "descending"}]},
  {"window": [{"op": "rank", "as": "rank"}]},
  {"fold": ["col_a", "col_b"], "as": ["key", "value"]},
  {"flatten": ["array_field"]},
  {"sample": 500},
  {"impute": "value", "key": "date", "method": "value", "value": 0}
]
```

## Filter expressions

```json
{"filter": "datum.year === 2020"}
{"filter": {"field": "Origin", "equal": "USA"}}
{"filter": {"field": "date", "range": ["2020-01-01", "2020-12-31"]}}
{"filter": {"field": "Origin", "oneOf": ["USA", "Japan"]}}
{"filter": {"field": "Horsepower", "valid": true}}
```

## CSV parse types

Force correct types when CSV auto-detection fails:

```json
"format": {
  "type": "csv",
  "parse": {
    "date": "date",
    "value": "number",
    "flag": "boolean"
  }
}
```
