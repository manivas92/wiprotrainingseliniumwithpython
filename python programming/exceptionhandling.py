try:
    a = int(input("enter the number"))
    b = int(input("enter the number"))
    print(a/b)
except ZeroDivisionError:
    print("cannot divide with zero")
except ValueError:
    print("please enter valid numbers")

try:
    a = 10/2
except Exception as e:
    print(e)
else:
    print("divison successfull")

finally:
    print("close the browser")

age = int(input("enter the age"))
if age < 21:
    raise ValueError("age must be 21 or above")
else:
    print("you can prossed")