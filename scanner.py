from stock_list import get_stock_list
from data_loader import download_stock_history
from indicators import calculate_macd
from screener import check_strategy


def scan_market(limit=None):
    """
    掃描股票
    limit=None 表示全部
    """

    stocks = get_stock_list()

    if limit:
        stocks = stocks.head(limit)

    results = []

    total = len(stocks)

    for index, row in stocks.iterrows():

        code = row["code"]
        name = row["name"]

        print(f"[{index+1}/{total}] {code} {name}")

        try:

            df = download_stock_history(code)

            df = calculate_macd(df)

            result = check_strategy(df)

            if result and result["pass"]:

                results.append({
                    "code": code,
                    "name": name,
                    "close": result["close"],
                    "high": result["high"],
                    "osc": result["osc"],
                    "osc_prev": result["osc_prev"],
                })

                print("    ✅ 符合")

            else:

                print("    ❌ 不符合")

        except Exception as e:

            print(f"    ⚠️ {e}")

    return results