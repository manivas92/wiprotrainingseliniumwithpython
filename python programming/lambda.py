add = lambda a,b: a+b
print(add(3,5))

square = lambda a: a*a
print(square(2))

evenorodd = lambda a: a%2 == 0
print(evenorodd(2))

maxim = lambda a,b: a if a > b else b
print(maxim(3,1))

numbers =[1,2,3,4,5,6]
odd = list(filter(lambda x: x%2  !=0, numbers))
print(odd)

numbers = [1,-1,2,-2,3,-3]
positive = list(filter(lambda x : x > 0 ,numbers))
print(positive)

data = ["hello", "", "world", "", "python"]
nonempty = list(filter(lambda x: x != "",data))
print(nonempty)

data = ["hello", "", "world", "", "python"]
empty = list(filter(lambda x: x == "", data))
print(empty)

from functools import reduce
nums = [10, 20, 30, 40]
print(reduce(lambda x, y: x + y, nums))

from functools import reduce
nums = [10, 20, 30, 40]
print(reduce(lambda x, y: x * y, nums))

from functools import reduce
nums = [10, 20, 30, 40]
print(reduce(lambda x,y: x if x>y else y, nums))

from functools import reduce
nums = [10, 20, 30, 40]
print(reduce(lambda x,y: x if x<y else y, nums))

nums = [10, 20, 30, 40]
squares = list(map(lambda x : x*x, nums))
print(squares)

data = [(1, 3), (4, 1), (2, 2)]
sorteddata = sorted(data, key=lambda x: x[0])
print(sorteddata)

marks = {"A": 75, "B": 90, "C": 60}
sorted_marks = dict(sorted(marks.items(), key=lambda x: x[1]))
print(sorted_marks)
