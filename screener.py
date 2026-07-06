import pandas as pd


def check_strategy(df: pd.DataFrame):

    if len(df) < 35:
        return None

    today = df.iloc[-1]
    yesterday = df.iloc[-2]

    close_today = float(today["Close"])
    high_yesterday = float(yesterday["High"])

    osc_today = float(today["OSC"])
    osc_yesterday = float(yesterday["OSC"])

    condition1 = close_today > high_yesterday
    condition2 = osc_today >= osc_yesterday

    return {
        "close": close_today,
        "high": high_yesterday,
        "osc": osc_today,
        "osc_prev": osc_yesterday,
        "condition1": condition1,
        "condition2": condition2,
        "pass": condition1 and condition2,
    }