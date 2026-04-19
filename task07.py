from products import products
variants = []

for product in products:
    variants.extend(product['variants'])

result = min(variants, key=lambda variant: variant['price'])
print(result)