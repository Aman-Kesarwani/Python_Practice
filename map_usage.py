products = [
    ("Prod_1", 10),
    ("Prod_2", 15),
    ("Prod_3", 2),
    ("Prod_4", 0)
]

prices = []

for product in products:
    prices.append(product[1])

print(prices)

# map function returns map object
products_map = map(lambda product: product[1], products)

for item in products_map:
    print(item)


# convert map to list is better way
products_list = list(map(lambda product: product[1], products))

print(products_list)
