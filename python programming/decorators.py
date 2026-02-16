def generator():
    print("printing 1")
    yield 1

    print("printing 2")
    yield 2

    print("printing 3")
    yield 3

    print("printing 4")
    yield 4

ret_value = generator()

print(next(ret_value))
print(next(ret_value))
print(next(ret_value))

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def vanillacake():
    print("I am the vanilla cake")

@make_pretty
def strawberrycake():
    print("I am the starberry cake")

vanillacake()
strawberrycake()