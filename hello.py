import pandas as pd
import plotly.express as px
import preswald

df = pd.read_csv('data/sales.csv')

preswald.text("# Sales Analytics Dashboard")
preswald.text("Visualizing sales data by product, category, and region.")

preswald.text("## Raw Data Table")
preswald.table(df)

preswald.text("## Total Revenue by Region")
region_rev = df.groupby('region', as_index=False)['revenue'].sum()
fig_region = px.bar(region_rev, x='region', y='revenue', title='Total Revenue by Region', text_auto=True)
preswald.plotly(fig_region)

preswald.text("## Sales Units by Category")
cat_sales = df.groupby('category', as_index=False)['sales_units'].sum()
fig_cat = px.pie(cat_sales, names='category', values='sales_units', title='Sales Units by Category')
preswald.plotly(fig_cat)

preswald.text("## Top Products by Revenue")
prod_rev = df.groupby('product', as_index=False)['revenue'].sum().sort_values('revenue', ascending=False)
fig_prod = px.bar(
    prod_rev,
    x='revenue',
    y='product',
    orientation='h',
    title='Top Products by Revenue',
    text_auto=True
)
preswald.plotly(fig_prod)

