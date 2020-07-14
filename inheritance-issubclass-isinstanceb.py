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

# Below cases print "True"
print(isinstance(mammal, object))
print(isinstance(mammal, Animal))
print(isinstance(mammal, Mammal))

# Below cases print "True"
print(issubclass(Mammal, object))
print(issubclass(Mammal, Animal))

# Below case prints "False"
print(issubclass(Mammal, Fish))

print(mammal.age)
mammal.eat()
o1 = object()
