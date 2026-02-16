
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=5):
    print(index, fruit)

word = "python"
for i, ch in enumerate(word):
    print(i,ch)

word = "python"
for i, ch in enumerate(word, start =3):
    print(i,ch)

fruits = ("apple", "banana", "cherry")
for index, fruit in enumerate(fruits):
    print(index, fruit)

test_cases = ["login","signup","checkout"]
for case_no, test in enumerate(test_cases , start=1):
    print(f"executing testcase {case_no}: {test}")

