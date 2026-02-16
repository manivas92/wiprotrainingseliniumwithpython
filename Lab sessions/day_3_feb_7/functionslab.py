def sum(a,b):
    return a + b

print(sum(3,5))

def maxm(n):
    return n % 10

nums = [1,5,7,4,9,3]
result = max(nums, key=maxm)
print(result)


