import re

text = "hello world"
result = re.match("hello",text)
print(result)

test_str = "1234567abcdeufgutijjabcABCT"
pattern = re.compile("abc")
matches = pattern.finditer(test_str)

for match in matches:
    print(match)

text = "python of powerful math powerful"
result = re.search("powerful",text)
print(result)

a = r"\tHello"
print(a)

my_string = "abc123ABC123abc"
pattern = re.compile(r'123')
matches = pattern.findall(my_string)

for match in matches:
    print(match)

test_string = '123abc456789abc123ABC'
pattern =re.compile(r'abc')
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
    print(match.span(),match.start(),match.end())
    print(match.group())

#\S Non whitespaces \S - Matches anything that is NOT space,tab,newline.
text = "hi there"
result = re.findall(r"\S",text)
print(result)

# \b Word boundary → Matches position at start or end of a word.
text = "cat scatter catalog"
result = re.findall(pattern=r"\bcat\b", string=text)
print(result)

# Matches only full word "cat"

# \B Not a word boundary → Matches when pattern is NOT at word boundary.
text = "cat scatter catalog"
result = re.findall(pattern=r"cat\B", string=text)
print(result)


