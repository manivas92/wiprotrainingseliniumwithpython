
class  Calculator:
    def add(selfs,a,b):
        print(a +b )

c = Calculator()
c.add(10,12)
c.add(20,14)

class Test:
    def run(self, browser = "chrome"):
        print("Running on", browser)

c = Test()
c.run()
c.run("firefox")

class Numbers:
    def total(self, *args):
        print(sum(args))

n = Numbers()
n.total(10,20,30)
n.total(10)
n.total(10,60)