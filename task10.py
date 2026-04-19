from products import products

res = {}
for product in products: 
    category = product['category']['name']
    if category not in res:
        res[category] = []

    res[category].append(product['name'])
print(res)