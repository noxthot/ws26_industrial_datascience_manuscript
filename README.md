# Industrial Data Science Course Material
This repository contains the course material for an Industrial Data Science course.

You can find the latest version of the course material at https://noxthot.github.io/ws26_industrial_datascience_manuscript/.

## Citing this manuscript
[![DOI](https://zenodo.org/badge/1035638412.svg)](https://zenodo.org/badge/latestdoi/1035638412)

If you use this material, please cite it by using the [citation information](./CITATION.cff).

## Content
- Time series
- Data imputation
- Clustering
- Classification
- Regression
- Batch and Stream Processing
- Exploratory Data Analysis
- Predictive Maintenance


## Setup
`uv` is used to manage the virtual environment and dependencies.

Then install the dependencies with:
```bash
uv sync --dev
```

## Local preview
To preview the manuscript locally, run:
```bash
uv run quarto preview
```
