---
name: vl-field-types
description: Vega-Lite v5 field type reference — quantitative, nominal, ordinal, temporal — and when to use each.
---

# Vega-Lite Field Types

Vega-Lite uses the field type to determine appropriate scales, axes, and legends.

## The four types

### `quantitative` (Q)
Continuous numeric measurements.

- **Use for:** prices, temperatures, counts, ratios, distances
- **Default scale:** linear, zero-based
- **Axis:** continuous ticks
- **Legend:** gradient color scale

```json
{"field": "Miles_per_Gallon", "type": "quantitative"}
```

### `nominal` (N)
Unordered categorical labels.

- **Use for:** names, countries, colors, boolean flags, IDs
- **Default scale:** ordinal, unordered
- **Axis:** categorical ticks
- **Legend:** discrete color swatches

```json
{"field": "Origin", "type": "nominal"}
```

### `ordinal` (O)
Ordered categorical values.

- **Use for:** ratings (1–5 stars), sizes (S/M/L/XL), education levels, survey Likert scales
- **Default scale:** ordinal, preserves order
- **Axis:** categorical ticks in order
- **Legend:** discrete color swatches (ordered)

```json
{"field": "Rating", "type": "ordinal"}
```

### `temporal` (T)
Date/time values.

- **Use for:** timestamps, dates, months, years
- **Default scale:** time scale
- **Axis:** time-aware tick formatting
- **Supports:** `timeUnit` for rounding

```json
{"field": "date", "type": "temporal"}
```

## Shorthand abbreviations

| Full name | Abbreviation |
|-----------|-------------|
| `quantitative` | `Q` |
| `nominal` | `N` |
| `ordinal` | `O` |
| `temporal` | `T` |

Shorthand: `"x": "date:T"` is equivalent to `"x": {"field": "date", "type": "temporal"}`.

## Time units for temporal fields

Use `timeUnit` to round or extract date components:

| timeUnit | Example output |
|----------|---------------|
| `year` | 2020, 2021 |
| `month` | Jan, Feb, … |
| `date` | 1, 2, … 31 |
| `day` | Mon, Tue, … |
| `hours` | 0, 1, … 23 |
| `yearmonth` | Jan 2020, Feb 2020 |
| `yearmonthdate` | Jan 1 2020 |
| `monthdate` | Jan 1, Jan 2, … |

```json
{"field": "timestamp", "type": "temporal", "timeUnit": "yearmonth"}
```

## Choosing the right type

| If the field is… | Use type |
|-----------------|----------|
| A number you can average | `quantitative` |
| A category with no order | `nominal` |
| A category with meaningful order | `ordinal` |
| A date, time, or datetime | `temporal` |
| A count of rows | `quantitative` (with `aggregate: "count"`) |
