products = [
    ("Prod_1", 10),
    ("Prod_2", 15),
    ("Prod_3", 2),
    ("Prod_4", 0)
]

filtered_items = filter(lambda item: item[1] >= 10, products)

for item in filtered_items:
    print(item)

filtered = list(filter(lambda item: item[1] >= 10, products))

print(filtered)
