products = [
    ("Prod_1", 10),
    ("Prod_2", 15),
    ("Prod_3", 2),
    ("Prod_4", 0)
]

# sort using labmbda
products.sort(key=lambda x: x[1])
print(products)
