from products import products

min_price = 50
max_price = 100

res = list(map(
    lambda p: p["name"],
    filter(lambda p: any(min_price <= v["price"] <= max_price
            for v in p["variants"]),products)))

print(res) 