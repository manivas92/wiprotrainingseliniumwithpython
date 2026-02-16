from functools import reduce

nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x%2 ==0, nums))
print(even)

nums = [1, 2, 3, 4, 5, 6]
squares = list(map(lambda x: x*x, nums))
print(squares)

nums = [1, 2, 3, 4, 5, 6]
sums = (reduce(lambda x,y: x+y, nums))
print(sums)

salaries = [25000, 40000, 32000, 18000]
sums = list(filter(lambda x: x>30000,salaries))
print(sums)
hike = (reduce(lambda x,y: x + y*0.10,sums))
print(hike)
print(hike)
total_payout = sum(map(lambda x: x * 1.10, filter(lambda x: x > 30000, hike)))