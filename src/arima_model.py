import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Loading the preprocessed data
from preprocessing import load_and_prepare_data
daily_sales = load_and_prepare_data()
print(daily_sales.head())

# set date as index 
daily_sales.set_index('Order Date', inplace=True)

# visualize time series
plt.figure(figsize=(10,5))
plt.plot(daily_sales['Sales'])
plt.title("Daily Sales Trend (ARIMA)")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("outputs/graphs/arima_trend.png")
plt.show()

#splitting the data
split = int(len(daily_sales) * 0.8)
train = daily_sales[:split]
test = daily_sales[split:]

# building ARIMA model
model = ARIMA(train["Sales"], order=(5,1,0))
model_fit = model.fit()
predictions = model_fit.forecast(steps=len(test))

#Evaluation
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

mae = mean_absolute_error(test["Sales"], predictions)
mse = mean_squared_error(test["Sales"], predictions)
rmse = np.sqrt(mse)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)

#actual vs predicted plot
plt.figure(figsize=(10,5))
plt.plot(test.index, test["Sales"], label="Actual")
plt.plot(test.index, predictions, label="Predicted (ARIMA)", color='red')
plt.legend()
plt.title("ARIMA: Actual vs Predicted (Test Data)")
plt.grid(True)
plt.savefig("outputs/graphs/arima_actual_vs_predicted.png")
plt.show()

# forecast next 30 days
forecast = model_fit.forecast(steps=30)
future_dates = pd.date_range(
    start=daily_sales.index.max() + pd.Timedelta(days=1),
    periods=30
)

forecast_df = pd.DataFrame({
    'Order Date': future_dates,
    'Predicted Sales': forecast.values
})

# Forecast Plotting
plt.figure(figsize=(10,5))
plt.plot(daily_sales.index, daily_sales['Sales'], label="Actual")
plt.plot(future_dates, forecast, label="ARIMA Forecast", color='red')
plt.legend()
plt.title("ARIMA Forecast (Next 30 Days)")
plt.grid(True)
plt.savefig("outputs/graphs/arima_forecast.png")
plt.show()

# separate forecast plot
plt.figure(figsize=(10,5))
plt.plot(future_dates, forecast, color='red')
plt.title("Future Sales Forecast (Next 30 Days - ARIMA)")
plt.xlabel("Date")
plt.ylabel("Predicted Sales")
plt.grid(True)
plt.savefig("outputs/graphs/arima_only_forecast.png")
plt.show()

# Saving Forecast
forecast_df.to_csv("outputs/forecast_arima.csv", index=False)

print("ARIMA Forecast saved successfully!")