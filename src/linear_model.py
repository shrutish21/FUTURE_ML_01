
#Loading the preprocessed data
from preprocessing import load_and_prepare_data
daily_sales= load_and_prepare_data()
print(daily_sales.head())

#understanding daily sales trend
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.plot(daily_sales['Order Date'], daily_sales['Sales'])
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("outputs/graphs/linear_daily_trend.png")
plt.show()


#feature engineering
daily_sales['month'] = daily_sales['Order Date'].dt.month
daily_sales['day'] = daily_sales['Order Date'].dt.day
daily_sales['day_of_week'] = daily_sales['Order Date'].dt.dayofweek
daily_sales['year']= daily_sales['Order Date'].dt.year

#shape of daily sales
print("Dataset shape:", daily_sales.shape)

#understanding the trend monthly
monthly_sales = daily_sales.groupby('month')['Sales'].sum()
plt.figure()
plt.bar(monthly_sales.index, monthly_sales.values)
plt.title("Monthly Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

#yearly trend
yearly_sales= daily_sales.groupby('year')['Sales'].sum()
plt.figure()
plt.bar(yearly_sales.index, yearly_sales.values)
plt.title("Yearly trend")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.show()

#Independent and Dependent variables
X = daily_sales[['year', 'month', 'day', 'day_of_week']]
y = daily_sales['Sales']

#splitting the data
split = int(len(X) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]
print("Training size:", len(X_train))
print("Testing size:", len(X_test))

#Model Building
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

#Evaluation
from sklearn.metrics import mean_absolute_error,mean_squared_error
import numpy as np
mae = mean_absolute_error(y_test, predictions)
print("MAE:", mae)
mse=mean_squared_error(y_test,predictions)
print("MSE:",mse)
rmse= np.sqrt(mse)
print("RMSE:",rmse)

#Plotting Actual vs predicted
plt.figure(figsize=(10,5))
plt.plot(range(len(y_test)), y_test.values, label="Actual")
plt.plot(range(len(predictions)), predictions, label="Predicted (Linear Regression)")
plt.legend()
plt.grid(True)
plt.title("Actual vs Predicted Sales")
plt.savefig("outputs/graphs/actual_vs_predicted_linear.png")
plt.show()

# future forecasting
import pandas as pd
future_dates = pd.date_range(start=daily_sales['Order Date'].max() + pd.Timedelta(days=1), periods=30)

future_df = pd.DataFrame()
future_df['Order Date'] = future_dates
future_df['year'] = future_df['Order Date'].dt.year
future_df['month'] = future_df['Order Date'].dt.month
future_df['day'] = future_df['Order Date'].dt.day
future_df['day_of_week'] = future_df['Order Date'].dt.dayofweek

future_predictions = model.predict(future_df[['year','month','day','day_of_week']])

#Forecast Plotting
plt.figure(figsize=(10,5))
plt.plot(daily_sales['Order Date'], daily_sales['Sales'], label="Actual")
plt.plot(future_df['Order Date'], future_predictions, label="Forecast", color='red')
plt.legend()
plt.title("Future Sales Forecast (Next 30 Days)")
plt.grid(True)
plt.savefig("outputs/graphs/linear_forecast.png")
plt.show()

# separate forecast plot (Linear Regression)
plt.figure(figsize=(10,5))
plt.plot(future_df['Order Date'], future_predictions, color='green')
plt.title("Future Sales Forecast (Next 30 Days - Linear Regression)")
plt.xlabel("Date")
plt.ylabel("Predicted Sales")
plt.grid(True)
plt.savefig("outputs/graphs/linear_only_forecast.png")
plt.show()

#saving forecast
future_df['Predicted Sales'] = future_predictions.round(2)
future_df.to_csv("outputs/forecast_linear.csv", index=False)
print("Forecast saved successfully!")