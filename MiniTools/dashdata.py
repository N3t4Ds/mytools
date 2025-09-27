import random

import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html
from dash.dependencies import Input, Output


# 模拟实时数据
def get_data():
    return pd.DataFrame({
        'time': pd.date_range(start='2023-01-01', periods=20, freq='H'),
        'value': [random.normalvariate(100, 15) for _ in range(20)]
    })


# 创建Dash应用
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("实时数据监控仪表板"),
    dcc.Graph(id='live-graph'),
    dcc.Interval(
        id='interval-component',
        interval=5 * 1000,  # 每5秒更新一次
        n_intervals=0
    )
])


@app.callback(
    Output('live-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph(n):
    df = get_data()
    fig = px.line(df, x='time', y='value', title='实时数据流')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
