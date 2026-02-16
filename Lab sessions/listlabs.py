#Write a Python program to get the largest number from a list.
a = {2,4,1,9,0,5,6}
i = max(a)
print(i)

#remove the even numbers from the lost
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers_list = [num for num in original_list if num % 2 != 0]

print(f"Original List: {original_list}")
print(f"List after removing even numbers: {odd_numbers_list}")

#multiply the items in the list
a = {2,4,1,9,5,6}
res = 1

for val in a:
    res = res * val

print(res)
