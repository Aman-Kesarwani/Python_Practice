class Animal:
    def __init__(self):
        self.age = 1
        print("Animal Constructor")

    def eat(self):
        print("eat")


class Mammal(Animal):

    def __init__(self):
        print("Mammal Constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


mammal = Mammal()
mammal.eat()
print(mammal.age)
print(mammal.weight)
