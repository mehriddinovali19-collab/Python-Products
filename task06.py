from products import products

res = list(map(lambda r: r['rating'],sum(map(lambda p: p['reviews'], products), [])))

print(res)