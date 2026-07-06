import pandas as pd
import requests

TWSE_URL = "https://openapi.twse.com.tw/v1/opendata/t187ap03_L"


def get_stock_list():

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(
        TWSE_URL,
        headers=headers,
        timeout=30
    )

    r.raise_for_status()

    if not r.text.strip():
        raise Exception("TWSE API 回傳空白內容")

    r.raise_for_status()

    print("HTTP Status:", r.status_code)
    print("Content-Type:", r.headers.get("Content-Type"))
    print("Response:")
    print(r.text[:500])

    df = pd.DataFrame(r.json())

    df = df.rename(columns={
        "公司代號": "code",
        "公司簡稱": "name",
    })

    return (
        df[["code", "name"]]
        .sort_values("code")
        .reset_index(drop=True)
    )