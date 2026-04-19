from products import products

res =   list(filter(lambda p: any( map(lambda v: v["inventory"]["stock"] == 0, p["variants"])
),products))

print(res)