class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())
from datetime import date

class Person:
    def __init__(self, name, country, year):
        self.name = name
        self.country = country
        self.year = year

    def age(self):
        current_year = date.today().year
        return current_year - self.year

p = Person("Manivas", "India", 2002)
print("Age:", p.age())

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def perimeter(self):
        return 2 * 3.14 * self.r


class Square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a * self.a

    def perimeter(self):
        return 4 * self.a


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

class Vehicle:
    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")


class Bus(Vehicle):
    def capacity(self):
        print("Bus capacity is 50")

b = Bus()
b.start()
b.capacity()
b.stop()

class Vehicle:
    pass
