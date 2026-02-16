from jinja2.debug import rewrite_traceback_stack


def printdata():
    print("hellomanivas")

printdata()

def printdata(name):
    print("hello",name)

printdata("varun")
printdata("sai")

def sqrt(numbers):
    result = numbers * numbers
    return  result

square = sqrt(2)
print("square of the number is :", square)
square = sqrt(3)
print("square of the number is :", square)

def add(num1, num2):
    sum = num1 + num2
    return sum

sums = add(2,5)
print("sum of two numbers is :",sums)

sums = add(122,29)
print("sum of two numbers is :",sums)

def fun_pass():
    pass

fun_pass()

def sort(n):
    n % 10
    return n

nums = [2,9,6,1,5]
result = (sorted(nums, key=sort))
print(result)

def even(limit):
    if limit % 2 ==0:
        print( "even")
    else:
        print("odd")

even(3)
even(6)

def areaofrect(len,wid):
    return len*wid

def areaofsq(side):
    return side*side

square = areaofrect(3,5)
print(areaofsq(square))