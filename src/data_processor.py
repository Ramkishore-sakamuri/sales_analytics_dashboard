import pandas as pd

def calculate_total_sales(df):
    """Calculates total sales for each order."""
    if 'Quantity' in df.columns and 'UnitPrice' in df.columns:
        df['TotalSale'] = df['Quantity'] * df['UnitPrice']
    return df

def aggregate_sales_by_category(df):
    """Aggregates total sales by product category."""
    if 'ProductCategory' in df.columns and 'TotalSale' in df.columns:
        return df.groupby('ProductCategory')['TotalSale'].sum().reset_index()
    return pd.DataFrame()

def aggregate_sales_over_time(df, time_period='M'): # 'M' for monthly
    """Aggregates total sales over a specified time period."""
    if 'OrderDate' in df.columns and 'TotalSale' in df.columns:
        # Ensure OrderDate is the index for resampling
        temp_df = df.set_index('OrderDate')
        return temp_df['TotalSale'].resample(time_period).sum().reset_index()
    return pd.DataFrame()

def get_quarterly_sales(df):
    """Calculates total sales per quarter."""
    if 'OrderDate' in df.columns and 'TotalSale' in df.columns:
        df['Quarter'] = df['OrderDate'].dt.to_period('Q').astype(str)
        quarterly_sales = df.groupby('Quarter')['TotalSale'].sum().reset_index()
        return quarterly_sales
    return pd.DataFrame()
