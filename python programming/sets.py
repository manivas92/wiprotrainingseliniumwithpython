# sets do not allow duplicate elements it contains only unique data
# unordered collection

# create a student_id set integer type
stu_id = {112, 113, 114, 115, 115}
print(stu_id)

# create a string type set
letters = {'a', 'b', 'c', 'd', 'e'}
print(letters)

# create a mixed set
mixed_set = {"Hello", 1, -7, 8.9}
print(mixed_set)

# create an empty set
empty_set = set()

# add
mixed_set.add(23)
print(mixed_set)

#remove
mixed_set.remove(8.9)
print(mixed_set)

mixed_set.pop()
print(mixed_set)

mixed_set.update()
print(mixed_set)

mixed_set.discard(23)
print(mixed_set)

a = {1,5,5,6,7}
b = {2,4,1,5,8,4}
c = a.difference(b)
print(c)

a = {1,5,5,6,7}
b = {2,4,1,5,8,4}
a.difference_update(b)
print(b)

a = {1,5,5,6,7}
b = {2,4,1,5,8,4}
c = a.intersection(b)
print(c)

a = {1,5,5,6,7}
b = {2,4,1,5,8,4}
a.intersection_update(b)
print(b)