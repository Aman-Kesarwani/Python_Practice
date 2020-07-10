products = [
    ("Prod_1", 10),
    ("Prod_2", 15),
    ("Prod_3", 2),
    ("Prod_4", 0)
]

prices = [product[1] for product in products]
print(prices)

filtered = [product for product in products if product[1] > 3]
print(filtered)
