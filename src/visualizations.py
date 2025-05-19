import plotly.express as px
import plotly.graph_objects as go

def create_sales_trend_chart(df_time_series, date_col='OrderDate', sales_col='TotalSale'):
    """Creates a line chart for sales trend over time."""
    if not df_time_series.empty:
        fig = px.line(df_time_series, x=date_col, y=sales_col, title='Sales Over Time')
        return fig
    return go.Figure().update_layout(title_text="No data for Sales Trend")

def create_sales_by_category_chart(df_category_sales, category_col='ProductCategory', sales_col='TotalSale'):
    """Creates a bar chart for sales by product category."""
    if not df_category_sales.empty:
        fig = px.bar(df_category_sales, x=category_col, y=sales_col, title='Sales by Product Category')
        return fig
    return go.Figure().update_layout(title_text="No data for Sales by Category")

def create_quarterly_sales_bar_chart(df_quarterly_sales, quarter_col='Quarter', sales_col='TotalSale'):
    """Creates a bar chart for quarterly sales."""
    if not df_quarterly_sales.empty:
        fig = px.bar(df_quarterly_sales, x=quarter_col, y=sales_col, title='Quarterly Sales Performance')
        # Potentially add growth calculation display here if you had previous period data
        return fig
    return go.Figure().update_layout(title_text="No data for Quarterly Sales")

def create_kpi_card(value, title, previous_value=None, currency_symbol='$', formatter="{}{:,.0f}"):
    """Creates a KPI indicator (e.g., for total sales or growth)."""
    delta = None
    if previous_value is not None and previous_value != 0:
        delta = ((value - previous_value) / previous_value) * 100

    fig = go.Figure()
    fig.add_trace(go.Indicator(
        mode = "number" + ("+delta" if delta is not None else ""),
        value = value,
        title = {"text": title},
        number = {'prefix': currency_symbol, 'valueformat': ',.0f'},
        delta = {'reference': previous_value, 'relative': True, 'valueformat': '.1%'} if delta is not None else None,
        domain = {'x': [0, 1], 'y': [0, 1]}
    ))
    fig.update_layout(height=200) # Adjust height as needed
    return fig
