from products import products

res = dict(
    map(lambda user: (user["id"], len(user["variants"])), products)
)
print(res)
