class Desc:
    def __get__(self, instance, owner):
        print("getting the value")
        return 10

class Test:
    x = Desc()

t = Test()
print(t.x)

class mydesc:
    def __get__(self, instance, owner):
        return  instance._value

    def __set__(self, instance, value):
        print("setting the value")
        instance._value = value

class Test:
    x = mydesc()

t = Test()
t.x = 100
print(t.x)

class Name:
    def __get__(self, instance, owner):
        return  instance._value

    def __set__(self, instance, value):
        instance._name = value

    def __delete__(self, instance):
        print("Deleting name")
        del instance._name

class Person():
    name = Name()

p = Person()
p.name = "manivas"
del p.name