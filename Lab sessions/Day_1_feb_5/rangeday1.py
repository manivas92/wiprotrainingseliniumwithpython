# 1. Check whether a number falls within a given range
a = range(5, 21)
num = 32

for i in a:
    if i == num:
        print("Number is within the range")
        break
else:
    print("Number is not within the range")


# 2. Print even numbers from 1 to 50
a = range (2,51,2)
for i in a:
    print(i)

# 3. Sum of numbers from 1 to 100
a = range (1,101)
sum = 0
for i in a:
    sum = sum+i

print(sum)


# 4. Print all numbers divisible by 5 between 1 and 100
a = range(5, 101,5)
for i in a:
    print(i)

# 5. Create a list of numbers from 50 to 100 with a step of 5
a = range (50,101,5)
for i in a:
    print(i)

# 6. Print the square of each number from 1 to 10
a = range(1,11)
for i in a:
    print(i*i)

# 7. Print numbers between -10 and 10
a = range(-10,10)
for i in a:
    print(i)

from functools import reduce
a = [1, 2, 2, 3]
print(len(a))
s = {1, 2, 2, 3}
print(len(s))