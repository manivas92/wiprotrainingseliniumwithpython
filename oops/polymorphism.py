print(len("python"))
print(len([1,2,3]))
print(len({1,2,3}))

class calculator:
    def add(self,a,b=0,c=0):
        return a+b+c

c = calculator()
print(c.add(5))
print(c.add(3,4,))
print(c.add(3,4,5))

class Animal:

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

a = Dog()
a.sound()