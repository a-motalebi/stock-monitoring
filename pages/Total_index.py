from utility import *
from dash import html, dcc, callback, Output, Input
import plotly.express as px
import dash
from postgres import connection
import datetime
import pytz
from dash.exceptions import PreventUpdate

dash.register_page(__name__, path="/", name="Total index")

cur = connection()
layout = html.Div(
    [
        dcc.Graph(id="Total index", figure=px.line(myData.out_df, x="time", y="index")),
        dcc.Interval(
            id="interval-component",
            interval=10 * 1000,  # in milliseconds
        ),
    ]
)


@callback(
    Output("Total index", "figure"),
    Input("interval-component", "n_intervals"),
)
def update_graph(value):

    # PreventUpdate prevents output updating
    now = datetime.datetime.now(tz=pytz.timezone("Asia/Tehran"))
    check_time(now)

    return px.line(myData.out_df, x="time", y="index")
