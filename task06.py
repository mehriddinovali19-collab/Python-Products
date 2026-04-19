from products import products

res = list(map(lambda rating: rating['rating'],sum(map(lambda p: p['reviews'], products), [])))

print(res)