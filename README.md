# Industrial Data Science Course Material
This repository contains the course material for an Industrial Data Science course.

You can find the latest version of the course material at https://noxthot.github.io/ws26_industrial_datascience_manuscript/.

## Citing this manuscript
[![DOI](https://zenodo.org/badge/1035638412.svg)](https://zenodo.org/badge/latestdoi/1035638412)

If you use this material, please cite it by using the [citation information](./CITATION.cff).

## Content
- Introduction: history and application areas of industrial data science
- Time series: imputation, decomposition, similarity measures, clustering, classification, and regression
- Predictive maintenance via exploratory data analysis
- Multimodal machine learning and fusion strategies
- Process optimization on sensor data
- Levels of system integration, batch and stream processing
- Live feedback via OPC UA
- Resampling
- Reinforcement learning


## Setup
[`uv`](https://docs.astral.sh/uv/) is used to manage the virtual environment and dependencies.

After installing `uv`, install the dependencies with:
```bash
uv sync --dev
```

## Local preview
To preview the manuscript locally, run:
```bash
uv run quarto preview
```
