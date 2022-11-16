# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Frutas": ["Uva", "Morango", "Bananas", "Uva", "Morango", "Bananas"],
    "Consumo unidade por dia": [4, 1, 6, 2, 8, 5],
    "Cidade": ["São Paulo", "São Paulo", "São Paulo", "Atibaia", "Atibaia", "Atibaia"]
})

fig = px.bar(df, x="Frutas", y="Montante", color="Cidade", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Meu Dash'),

    html.Div(children='''
        Dash: Meu exemplo de comparativo de consumo de frutas Atibaia - São Paulo.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
