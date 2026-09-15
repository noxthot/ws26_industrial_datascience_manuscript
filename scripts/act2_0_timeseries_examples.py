# %%
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
from scipy.datasets import electrocardiogram
from statsmodels.datasets import get_rdataset

# %%
# Example datasets: AirPassengers, Synthetic Sine Wave, CO2, Mauna Loa, Random Walk, Stock Market, Health Sciences

# AirPassengers (from statsmodels)
try:
    air = get_rdataset("AirPassengers").data
    air_series = pd.Series(
        air["value"].values, index=pd.date_range("1949-01", periods=len(air), freq="MS")
    )
except OSError:
    air_series = pd.Series()

# Mauna Loa CO2 (from statsmodels)
try:
    from statsmodels.datasets import co2 as sm_co2

    mauna = sm_co2.load_pandas().data
    mauna.index = pd.date_range("1958-03", periods=len(mauna), freq="W")
    mauna_series = mauna["co2"]
except OSError:
    mauna_series = pd.Series()

# Random Walk (synthetic)
np.random.seed(0)
random_walk = np.cumsum(np.random.randn(200))
random_walk_series = pd.Series(random_walk, index=pd.RangeIndex(len(random_walk)))

# Stock Market Example (e.g., S&P 500)
try:
    sp500 = yf.download("^GSPC", start="2020-01-01", end="2021-01-01", auto_adjust=True)
    sp500_series = sp500["Close"]
except OSError:
    sp500_series = pd.Series()

# Health Sciences Example (e.g., Heart Rate from scipy.misc.electrocardiogram)

# Load ECG signal
heart_series = pd.Series(electrocardiogram())[:3000]

# Plotting
series_list = [
    ("AirPassengers", air_series),
    ("Mauna Loa CO2", mauna_series),
    ("Random Walk", random_walk_series),
    ("S&P 500 Close (2020)", sp500_series),
    ("Electrocardiogram", heart_series),
]

# %%
path = os.path.join("data", "assets", "act3")

for title, series in series_list:
    fig, ax = plt.subplots(figsize=(10, 3))
    if not series.empty:
        ax.plot(series)
        ax.set_title(title)
    else:
        ax.text(0.5, 0.5, f"{title} dataset not available", ha="center", va="center")
        ax.set_title(title)
    plt.tight_layout()
    filename = f"{title.lower().replace(' ', '_').replace('(', '').replace(')', '').replace('&', 'and')}.png"
    plt.savefig(os.path.join(path, filename))
    plt.close(fig)

# %%
