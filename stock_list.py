import pandas as pd
import requests

TWSE_URL = "https://openapi.twse.com.tw/v1/opendata/t187ap03_L"

def get_stock_list():
    r = requests.get(TWSE_URL, timeout=30)
    r.raise_for_status()

    df = pd.DataFrame(r.json())

    df = df.rename(columns={
        "公司代號": "code",
        "公司簡稱": "name",
    })

    return df[["code", "name"]].sort_values("code").reset_index(drop=True)