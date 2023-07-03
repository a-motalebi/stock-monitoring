from utility import *
from dash import html, dcc, callback, Output, Input
import plotly.express as px
import dash
import pytz
from dash.exceptions import PreventUpdate
import datetime


dash.register_page(__name__, path="/Funds", name="Funds index")


layout = html.Div(
    [
        dcc.Graph(
            id="Funds index", figure=px.line(myData.out_funds, x="time", y="index")
        ),
        dcc.Interval(
            id="interval-component",
            interval=10 * 1000,  # in milliseconds
        ),
    ]
)


@callback(
    Output("Funds index", "figure"),
    Input("interval-component", "n_intervals"),
)
def update_graph(value):

    # PreventUpdate prevents output updating
    now = datetime.datetime.now(tz=pytz.timezone("Asia/Tehran"))
    check_time(now)

    return px.line(myData.out_funds, x="time", y="index")
