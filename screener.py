import pandas as pd


def check_strategy(day_df: pd.DataFrame, month_df: pd.DataFrame):

    # 日K至少要有足夠資料才能計算MACD
    if len(day_df) < 35:
        return None

    # 月K至少需要兩個月才能比較OSC
    if len(month_df) < 2:
        return None

    # ---------- 日K ----------
    today = day_df.iloc[-1]
    yesterday = day_df.iloc[-2]

    close_today = float(today["Close"])
    close_yesterday = float(yesterday["Close"])
    high_yesterday = float(yesterday["High"])

    osc_today = float(today["OSC"])
    osc_yesterday = float(yesterday["OSC"])

    # ---------- 月K ----------
    month_now = month_df.iloc[-1]
    month_prev = month_df.iloc[-2]

    month_osc = float(month_now["OSC"])
    month_osc_prev = float(month_prev["OSC"])

    # ---------- 漲跌幅 ----------
    change_percent = round(
        (close_today - close_yesterday)
        / close_yesterday * 100,
        2
    )

    # ---------- 選股條件 ----------
    # 1. 收盤突破昨日最高價(包含上影線)
    condition1 = close_today > high_yesterday

    # 2. 日MACD OSC持續走強
    condition2 = osc_today >= osc_yesterday

    # 3. 月MACD OSC不得轉弱
    condition3 = month_osc >= month_osc_prev

    passed = (
        condition1
        and condition2
        and condition3
    )

    return {
        "pass": passed,

        "close": round(close_today, 2),
        "high": round(high_yesterday, 2),

        "osc": round(osc_today, 4),
        "osc_prev": round(osc_yesterday, 4),

        "month_osc": round(month_osc, 4),
        "month_osc_prev": round(month_osc_prev, 4),

        "change_percent": change_percent,

        "condition1": condition1,
        "condition2": condition2,
        "condition3": condition3,
    }