class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Child, Sub


class Mammal(Animal):
    def walk(self):
        print("walk")

# Child, Sub


class Fish(Animal):
    def swim(self):
        print("swim")


mammal = Mammal()
print(mammal.age)
mammal.eat()
