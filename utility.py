import pandas as pd
from postgres import connection
from dash.exceptions import PreventUpdate

###### Return index of all input dataframe
def index(df):
    return (df["last_return"] * df["value"]).sum() / df["value"].sum()


###### Filter Funds from all
def Funds(df):
    mask = df[["isin"]].apply(lambda x: x.str.contains("^IRT", regex=True)).any(axis=1)
    return df[mask]


def check_time(now):
    if (
        now.weekday() == 3
        or now.weekday() == 4
        or now.hour < 9
        or now.hour > 12
        or (now.hour >= 12 and now.minute > 30)
    ):
        raise PreventUpdate


class myData:
    out_df = pd.DataFrame(data={"index": [], "time": []})
    out_funds = pd.DataFrame(data={"index": [], "time": []})

    ## Postgresql connection
    cur = connection()
