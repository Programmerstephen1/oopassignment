# Base class Animal
class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class Dog
class Dog(Animal):
    def move(self):
        print("The dog runs on all fours! 🐕")

# Derived class Cat
class Cat(Animal):
    def move(self):
        print("The cat gracefully walks on four legs. 🐈")

# Derived class Bird
class Bird(Animal):
    def move(self):
        print("The bird flies in the sky. 🕊️")

# Derived class Car
class Car:
    def move(self):
        print("The car drives on the road. 🚗")

# Derived class Plane
class Plane:
    def move(self):
        print("The plane flies through the air. ✈️")

# Create instances of each class
dog = Dog()
cat = Cat()
bird = Bird()
car = Car()
plane = Plane()

# Demonstrate polymorphism
animals = [dog, cat, bird]
for animal in animals:
    animal.move()

vehicles = [car, plane]
for vehicle in vehicles:
    vehicle.move()
