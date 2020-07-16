class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Person, Employee):
    pass


manager = Manager()
manager.greet()  # Person greet will be called as per order of inheritance

###########


class FlyingCreature:
    def fly(self):
        print("Fly")


class SwimmingCreature:
    def swim(self):
        print("swim")


class FlyingFish(FlyingCreature, SwimmingCreature):
    def eat(self):
        print("Eat")


fish = FlyingFish()
fish.fly()
fish.swim()
fish.eat()
