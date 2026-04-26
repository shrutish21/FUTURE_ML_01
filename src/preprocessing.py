import pandas as pd

def load_and_prepare_data():
    # load dataset
    df = pd.read_csv("data/Superstore.csv", encoding="latin1")

    # select required columns
    df = df[['Order Date', 'Sales']].copy()

    # convert to datetime
    df['Order Date'] = pd.to_datetime(df['Order Date'])

    # aggregate daily sales
    daily_sales = df.groupby('Order Date')['Sales'].sum().reset_index()

    # sort by date
    daily_sales = daily_sales.sort_values('Order Date')
    daily_sales.sort_index(inplace=True)

    return daily_sales