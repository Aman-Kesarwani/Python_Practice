class Commodity:
    def __init__(self, price):
        self.__set_price(price)

    def __get_price(self):
        return self.__price

    def __set_price(self, value):
        if value < 0:
            raise ValueError("How can price be negative?")
        self.__price = value

    price = property(__get_price, __set_price)


commodity = Commodity(10)
print(commodity.price)
commodity.price = 50
print(commodity.price)
