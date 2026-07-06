from exporter import save_result
from scanner import scan_market

from config import TEST_MODE, TEST_LIMIT

if TEST_MODE:
    results = scan_market(limit=TEST_LIMIT)
else:
    results = scan_market()

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

save_result(results)