import pandas as pd

def load_sales_data(file_path='data/sample_sales_data.csv'):
    """Loads sales data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        df['OrderDate'] = pd.to_datetime(df['OrderDate'])
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return pd.DataFrame() # Return empty DataFrame on error

# Example for loading from a hypothetical database (requires more setup)
# from sqlalchemy import create_engine
# def load_from_db(db_connection_string):
#     engine = create_engine(db_connection_string)
#     query = "SELECT * FROM sales_fact_table;"
#     df = pd.read_sql(query, engine)
#     df['OrderDate'] = pd.to_datetime(df['OrderDate'])
#     return df
