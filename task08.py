from products import products

res = list(
    map(
        lambda p: {
            "name": p["name"],
            "average_rating": (
                sum(map(lambda r: r.get("rating", 0), p.get("reviews", [])))
                / len(p.get("reviews", []))
                if p.get("reviews") else 0)}, products ))

print(res)
