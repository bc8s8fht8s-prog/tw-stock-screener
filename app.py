from scanner import scan_market

results = scan_market(limit=10)

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