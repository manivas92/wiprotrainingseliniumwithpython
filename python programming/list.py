empty_list =[]
number = [1,2,3,5,7,4,2,3,1]
mixed_data = [1,"hello",True, 5.6 ]
nested = [[1,2],[3,4]]

print(mixed_data[1])
print(mixed_data[2])

mixed_data[3]= 26
print(mixed_data)

mixed_data.insert(0,11)
print(mixed_data)

mixed_data.append("mani")
print(mixed_data)

mixed_data.remove("hello")
print(mixed_data)

mixed_data.pop(2)
print(mixed_data)

number.sort()
print(number)

number.reverse()
print(number)

print(number.count(2))

print(number.index(3))

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']

print(my_list[2:5])
print(my_list[5:])
print(my_list[:])

nums = [10, 20, 30, 40, 50]

print(nums[0])
print(nums[-2])

numbers = [1, 3, 5]
even_numbers = [2, 4, 6]

numbers.extend(even_numbers)
print(numbers)
