import pandas as pd


def calculate_macd(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df["EMA12"] = df["Close"].ewm(span=12, adjust=False).mean()
    df["EMA26"] = df["Close"].ewm(span=26, adjust=False).mean()

    df["DIF"] = df["EMA12"] - df["EMA26"]
    df["MACD"] = df["DIF"].ewm(span=9, adjust=False).mean()

    df["OSC"] = df["DIF"] - df["MACD"]

    return df


def calculate_month_macd(df: pd.DataFrame) -> pd.DataFrame:
    """
    將日K轉成月K後，再計算月MACD
    """

    month_df = df.copy()

    month_df["Date"] = pd.to_datetime(month_df["Date"])
    month_df.set_index("Date", inplace=True)

    month_df = month_df.resample("ME").agg({
        "Open": "first",
        "High": "max",
        "Low": "min",
        "Close": "last",
        "Volume": "sum"
    })

    month_df.dropna(inplace=True)

    month_df["EMA12"] = month_df["Close"].ewm(span=12, adjust=False).mean()
    month_df["EMA26"] = month_df["Close"].ewm(span=26, adjust=False).mean()

    month_df["DIF"] = month_df["EMA12"] - month_df["EMA26"]
    month_df["MACD"] = month_df["DIF"].ewm(span=9, adjust=False).mean()
    month_df["OSC"] = month_df["DIF"] - month_df["MACD"]

    return month_df