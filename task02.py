from products import products

res = list(map(lambda name: {'name': name['name']}, products ))
print(res)