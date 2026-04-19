from products import products

res = list(map(lambda user: {"name": user['name'], "active": user['is_active']},
                filter(lambda user: user['is_active'], products )))
print(res)


