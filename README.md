# 📊 Sales Forecasting using Machine Learning

## 🔍 Project Overview
This project analyzes historical sales data and predicts future sales using two approaches:
- **Linear Regression (Machine Learning)**
- **ARIMA (Time Series Forecasting)**

The objective is to compare both models and understand their effectiveness in real-world business scenarios.

---

## 📁 Dataset
- Dataset: **Superstore Sales Dataset**
- Features used:
  - Order Date
  - Sales
- Data is aggregated at a **daily level** for time series analysis.

---

## ⚙️ Data Preprocessing
- Converted `Order Date` to datetime format
- Aggregated total sales per day
- Sorted data chronologically
- Feature engineering (for Linear Regression):
  - Year
  - Month
  - Day
  - Day of Week

---

## 🤖 Models Implemented

### 1️⃣ Linear Regression
- Uses date-based features to predict sales
- Captures general trends and seasonality
- Simple and stable model

### 2️⃣ ARIMA Model
- Time series forecasting model
- Uses past values to predict future values
- Configuration used: **ARIMA(5,1,0)**

---

## 📈 Model Evaluation

| Model              | MAE   | RMSE  |
|--------------------|-------|-------|
| Linear Regression  | 1756  | 2386  |
| ARIMA              | 1728  | 2655  |

---

## 🔎 Observations
- ARIMA has slightly **lower MAE**, indicating better average accuracy
- Linear Regression has **lower RMSE**, meaning fewer large errors
- ARIMA captures short-term patterns well but can be unstable
- Linear Regression provides smoother and more stable predictions

---

## 📊 Visualizations
The project includes:
- Daily Sales Trend
- Actual vs Predicted (Linear Regression & ARIMA)
- Future Forecast (30 days)
- Separate Forecast Graphs for better clarity

---

## 🔮 Forecasting
- Forecasted **next 30 days of sales** using both models
- Separate plots used to avoid scaling issues

### ⚠️ Important Insight
ARIMA forecasts tend to flatten over long durations (e.g., 365 days) due to lack of new patterns. Therefore, short-term forecasting is more reliable.

---

## ⚖️ Model Comparison

| Aspect              | Linear Regression        | ARIMA                     |
|---------------------|-------------------------|---------------------------|
| Type                | Machine Learning        | Time Series               |
| Input               | Engineered features     | Past values only          |
| Strength            | Stability               | Pattern detection         |
| Weakness            | Ignores time dependency | Sensitive to noise        |
| Best Use Case       | Long-term trend         | Short-term forecasting    |

---

## 💡 Business Insights & Conclusions

- **Short-Term Planning:**  
  ARIMA is better for short-term demand forecasting due to trend capturing.

- **Long-Term Strategy:**  
  Linear Regression is more stable and suitable for long-term predictions.

- **Inventory Management:**  
  Helps maintain optimal stock levels and reduce losses.

- **Sales Planning:**  
  Enables businesses to prepare for demand fluctuations.

- **Decision Making:**  
  Using both models together provides better insights.

---

## 🚀 Future Improvements
- Tune ARIMA parameters (p, d, q)
- Try advanced models like LSTM or Prophet
- Include external factors (holidays, promotions)
- Deploy as a web application

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Matplotlib
- Scikit-learn
- Statsmodels

---

## 📌 Conclusion
Both models provide valuable insights. ARIMA is useful for capturing time-based patterns, while Linear Regression ensures stable predictions. A combined approach can improve business decision-making.

---

## 🙌 Author
- Shruti Shinde