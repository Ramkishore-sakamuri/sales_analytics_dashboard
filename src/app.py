from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from data_loader import load_sales_data
from data_processor import calculate_total_sales, aggregate_sales_by_category, aggregate_sales_over_time, get_quarterly_sales
from visualizations import create_sales_trend_chart, create_sales_by_category_chart, create_quarterly_sales_bar_chart, create_kpi_card
from dashboard_layout import create_layout

# --- 1. Load and Prepare Data ---
df_raw = load_sales_data() # Use your actual data loading function
df_processed = calculate_total_sales(df_raw.copy())

# Aggregate data for visualizations
df_sales_trend = aggregate_sales_over_time(df_processed, time_period='M') # Monthly trend
df_category_sales = aggregate_sales_by_category(df_processed)
df_quarterly_sales = get_quarterly_sales(df_processed)

# --- Calculate KPIs (Example) ---
total_sales_current_period = df_processed['TotalSale'].sum()

# For quarterly growth, you'd need data from the previous quarter
# This is a simplified example assuming you have it or can calculate it.
# Let's simulate for now:
current_quarter_sales = 0
previous_quarter_sales = 0 # You would need to calculate this properly

if not df_quarterly_sales.empty:
    # Assuming df_quarterly_sales is sorted by Quarter
    if len(df_quarterly_sales) > 0:
        current_quarter_sales = df_quarterly_sales['TotalSale'].iloc[-1]
    if len(df_quarterly_sales) > 1:
        previous_quarter_sales = df_quarterly_sales['TotalSale'].iloc[-2]


# --- 2. Create Initial Figures ---
fig_sales_trend = create_sales_trend_chart(df_sales_trend)
fig_category_sales = create_sales_by_category_chart(df_category_sales)
fig_quarterly_sales = create_quarterly_sales_bar_chart(df_quarterly_sales)

# KPI Figures
kpi_total_sales_fig = create_kpi_card(total_sales_current_period, "Total Sales")
kpi_quarterly_growth_fig = create_kpi_card(current_quarter_sales, "Current Quarter Sales", previous_value=previous_quarter_sales)


# --- 3. Initialize Dash App ---
# Using Bootstrap for styling
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX]) # You can choose other themes
server = app.server # For deployment (e.g., on Heroku, Vercel)

app.layout = create_layout(fig_sales_trend, fig_category_sales, fig_quarterly_sales, kpi_total_sales_fig, kpi_quarterly_growth_fig)

# --- 4. Define Callbacks (for interactivity - not shown in detail here but crucial) ---
# Example:
# @app.callback(
#     Output('some-chart', 'figure'),
#     [Input('year-dropdown', 'value'), Input('region-dropdown', 'value')]
# )
# def update_chart(selected_year, selected_region):
#     # Filter data based on inputs
#     # Re-generate chart
#     return new_figure

# --- 5. Run the App ---
if __name__ == '__main__':
    app.run_server(debug=True)
