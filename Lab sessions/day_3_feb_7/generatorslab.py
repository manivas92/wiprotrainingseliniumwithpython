def numbers(n):
    for i in range(1, n+1):
        yield i

for x in numbers(5):
    print(x)

def even_numbers(n):
    for i in range(2, n+1, 2):
        yield i

for e in even_numbers(10):
    print(e)

def read_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line

#for line in read_file("sample.txt"):
   # print(line)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for f in fibonacci(7):
    print(f)

def retry():
    for attempt in range(1, 4):
        yield f"Attempt {attempt}"

for r in retry():
    print(r)
