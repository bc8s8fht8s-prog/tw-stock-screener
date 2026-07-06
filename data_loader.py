import yfinance as yf
import pandas as pd
from logger import log


def download_stock_history(stock_id: str) -> pd.DataFrame:
    """
    下載股票最近六個月歷史資料
    """

    symbol = f"{stock_id}.TW"

    log(f"下載 {symbol}")

    df = yf.download(
        symbol,
        period="6mo",
        auto_adjust=False,
        progress=False,
    )

    if df.empty:
        raise Exception(f"{stock_id} 無資料")

    df.reset_index(inplace=True)

    # yfinance 新版可能回傳 MultiIndex 欄位
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0] for col in df.columns]

    return df