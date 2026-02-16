names = ["Tom", "Jerry", "Spike"]
for i, n in enumerate(names):
    print(i, n)

nums = [5, 10, 15]
for i, v in enumerate(nums, start=1):
    print(i, v)

word = "CODE"
for i, ch in enumerate(word):
    print(i, ch)

data = (100, 200, 300)
for i, v in enumerate(data):
    print(i, v)

for i, v in enumerate(range(1, 6)):
    print(i, v)

colors = ["red", "green", "blue"]
for i, c in enumerate(colors, start=2):
    print(i, c)

items = []
for i, v in enumerate(items):
    print(i, v)

for i in enumerate(["x", "y", "z"]):
    print(i)

letters = "AB"
for i, v in enumerate(letters, start=5):
    print(i, v)

nums = [100, 200, 300]
for i, v in enumerate(nums, start=-1):
    print(i, v)

