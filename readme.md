
# Weighted Moving Average Time Series Forecasting

This repository hosts a Python implementation of the Weighted Moving Average (WMA) method for time series forecasting. The WMA is a statistical method that assigns different weights to historical data points, providing a means to more accurately reflect the contribution of each data point to the forecast.

## Overview

The project contains scripts for preprocessing time series data, computing weighted moving averages as forecasts, and evaluating the performance of the forecasts using the root mean square error (RMSE) metric.

## Project Structure

```
TIME-SERIES-FORECASTING/
│
├── data/
│   ├── train/
│   └── valid/
│
├── myenv/
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── share/
│
├── notebook/
│   └── Weighted_Moving_Average.ipynb
│
├── scripts/
│   └── time_series_weighted_moving_avg.py
│
├── .gitignore
├── readme.md
└── requirements.txt
```

## Requirements

To run the scripts, the following Python packages are required:
- `pandas`: For data manipulation and analysis.
- `numpy`: For numerical computations.
- `matplotlib`: For data visualization.
- `scikit-learn`: For calculating the RMSE.

These dependencies can be installed using the following command:
```sh
pip install -r requirements.txt
```

## Usage

Ensure you have Python installed and the above requirements satisfied. To execute the main script, run:
```sh
python scripts/time_series_weighted_moving_avg.py
```

Alternatively, you can run the Jupyter notebook `Weighted_Moving_Average.ipynb` for an interactive experience and to visualize the forecasts.

## Forecasting Process

1. Data is preprocessed to convert date strings to datetime objects and set as indices.
2. A list of the last seven values from the training data is created along with corresponding weights.
3. A weighted moving average is calculated for the validation data.
4. Forecasts are visualized compared to the actual data.
5. The RMSE is computed to assess the forecast accuracy.

## Visualizations

The script generates plots that compare the actual counts with the forecasts to visualize the performance of the weighted moving average method.

## Contributions

Contributions are welcome. Please feel free to submit a pull request or create an issue for any bugs or improvements.

## License

This project is open-sourced and available under the MIT License.

