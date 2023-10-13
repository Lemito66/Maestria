import pandas as pd
import plotly.express as px
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash import html

# Tu código de preparación de datos aquí (importación de datos, transformaciones, etc.)
df = pd.read_excel('https://github.com/mayait/ClaseAnalisisDatos/raw/main/eda/superstore.xlsx')
# Primero, convierte la columna 'Sales' a números (flotantes)
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

# Luego, elimina las filas con valores nulos en la columna 'Sales'
df = df.dropna(subset=['Sales'])
# Calcula las métricas
total_sales = df['Sales'].sum()
profit_sales_ratio = df['Profit'].sum() / total_sales
total_orders = df['Order ID'].nunique()

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Tu código para crear los gráficos aquí
# Agrupamos por mes y sumamos las ventas
# Agrupamos por 'Segment' y sumamos las ventas
sales_by_segment = df.groupby('Segment')['Sales'].sum().reset_index()

# Creamos el gráfico de barras con plotly.express
fig_sales_by_segment = px.bar(
    sales_by_segment,
    x='Segment',
    y='Sales',
    color='Segment',
    title='Ventas Totales por Segmento')

# Muestra el gráfico
#fig_sales_by_segment.show()


# Creamos el gráfico con plotly.express


# Muestra el gráfico
#fig_sales_order_date.show()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([

    html.H1("SUPERSTORE DASHBOARD", className="text-center my-4"),

    dbc.Row([
        # Primer bloque: Sumatoria de 'Sales'
        dbc.Col([
            html.H4("Ventas totales"),
            html.H1(f"${total_sales:,.0f}")
        ], width=4),

        # Segundo bloque: Cociente entre sumatoria de 'Profit' y 'Sales'
        dbc.Col([
            html.H4("Beneficios"),
            html.H1(f"{profit_sales_ratio:.0%}")
        ], width=4),

        # Tercer bloque: Cantidad de órdenes
        dbc.Col([
            html.H4("Ordenes totales"),
            html.H1(total_orders)
        ], width=4)
    ]),

    # Segunda fila
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig_sales_by_segment)
        ]),
        dbc.Col([
            dcc.Graph(figure=fig_sales_by_segment)
        ]),
        dbc.Col([
            dcc.Graph(figure=fig_sales_by_segment)
        ]),

    ]),
])



if __name__ == '__main__':
    app.run_server(debug=True)