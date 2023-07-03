from dash import Dash, html, dcc, callback, Output, Input
import dash
from utility import *
import pandas as pd
from hermes import Market_with_askbid
import datetime
import pytz
from dash.exceptions import PreventUpdate

app = Dash(__name__, use_pages=True)

app.layout = html.Div(
    [
        html.H1(children="HermesCapital", style={"textAlign": "center"}),
        html.Div(id="dummy"),
        html.Div(
            [
                html.Div(
                    dcc.Link(
                        f"{page['name']}",
                        href=page["relative_path"],
                    ),
                    style={"textAlign": "center"},
                )
                for page in dash.page_registry.values()
            ]
        ),
        dcc.Interval(
            id="interval-component",
            interval=10 * 1000,  # in milliseconds
        ),
        dash.page_container,
    ]
)


@callback(
    Output("dummy", "children"),
    Input("interval-component", "n_intervals"),
)
def update_graph(value):

    # PreventUpdate prevents output updating
    now = datetime.datetime.now(tz=pytz.timezone("Asia/Tehran"))
    check_time(now)

    df = Market_with_askbid()
    my_fund = Funds(df)

    ind = index(df)
    df2 = pd.DataFrame(
        [[ind, now]],
        columns=["index", "time"],
    )
    myData.cur.execute(
        "INSERT INTO total_index (time, index) VALUES (%s,%s)",
        (now, ind),
    )
    myData.out_df = myData.out_df.append(df2)

    ind = index(my_fund)
    myData.cur.execute(
        "INSERT INTO funds_index (time, index) VALUES (%s,%s)",
        (now, ind),
    )
    df2 = pd.DataFrame(
        [[ind, now]],
        columns=["index", "time"],
    )
    myData.out_funds = myData.out_funds.append(df2)

    return None


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)
