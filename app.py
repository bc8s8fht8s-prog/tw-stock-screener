from exporter import save_result
from scanner import scan_market

from config import TEST_MODE, TEST_LIMIT

# 執行掃描
if TEST_MODE:
    scan_data = scan_market(limit=TEST_LIMIT)
else:
    scan_data = scan_market()

# 取得掃描結果
results = scan_data["results"]
scan_count = scan_data["scan_count"]

print(results)

print()
print("=" * 40)
print("符合條件股票")
print("=" * 40)

if len(results) == 0:
    print("沒有符合條件")
else:
    for stock in results:
        print(stock["code"], stock["name"])

print()
print("共", len(results), "檔")
print("掃描股票", scan_count, "檔")

# 輸出 JSON
save_result(results, scan_count)