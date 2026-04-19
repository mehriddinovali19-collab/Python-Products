from products import products

query = "iphone"

res = list(filter(lambda p: query.lower() in p["name"].lower(), products))
print(res)