products = [
    ("Prod_1", 10),
    ("Prod_2", 15),
    ("Prod_3", 2),
    ("Prod_4", 0)
]


def sort_products(product):
    return product[1]  # second element of tuple


products.sort(key=sort_products)  # sort based on the second element - integer
print(products)
