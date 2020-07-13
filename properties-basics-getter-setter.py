class Commodity:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("How can price be negative?")
        self.__price = value


commodity = Commodity(10)
print(commodity.price)
commodity.price = 50
print(commodity.price)
