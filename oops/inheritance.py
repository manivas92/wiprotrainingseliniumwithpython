#single
class Employee:
    def __init__(self,name,empid):
        self.name = name
        self.empid = empid

    def empdetails(self):
        print(self.name,self.empid)

class Manager(Employee):

    def approve_leave(self):
        print("leave approved")

a = Manager("manivas",98989)
a.empdetails()
a.approve_leave()

class savingsaccount:
    def deposit(self):
        self.amount = int(input("Enter amount"))
        print("Your balance is ",self.amount)

    def interest(self):
        intersets = self.amount * 0.10
        print("intrest of the amount is",intersets)

a = savingsaccount()
a.deposit()
a.interest()

#mutlilevel
class savingsaccount:
    def deposit(self):
        self.amount = int(input("Enter amount"))
        print("Your balance is ",self.amount)

    def interest(self):
        intersets = self.amount * 0.10
        print("intrest of the amount is",intersets)

    def totalbalance(self):
        total = self.amount * 10 + self.amount
        print("Total amount is ",total)

a = savingsaccount()
a.deposit()
a.interest()
a.totalbalance()

#hierarchy
class Employee:

    def login(self):
        print("Employee is logged in")

class Developer(Employee):

    def write_code(self):
        print("writing code")

class Tester(Employee):

    def test_app(self):
        print("Test the application")

a = Developer()
test = Tester()

a.login()
a.write_code()
test.login()
test.test_app()

#multiple
class parent1:
    pass

class parent2:
    pass

class child(parent1,parent2):
    pass

class Father:
    def driving(self):
        print("Father has the skills to drive")

class Mother:
    def cooking(self):
        print("mother has the skills to cook")

class Child(Father,Mother):
    def bothskills(self):
        print("child has skills to study")
        print("Child has both skills of driving and cooking")

c = Child()
c.driving()
c.cooking()
c.bothskills()