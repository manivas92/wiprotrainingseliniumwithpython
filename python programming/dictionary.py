my_dict = {1: "One", 2 : "two"}
print(my_dict)
print(my_dict.get(1))

country = {
    "india": "Delhi",
    "canada": "ottawa",
    "england":"london"
}
print(country)

print(country["india"])

country["italy"]="rome"
print(country)

country["srilanka"]="colombo"
print(country)

del country["canada"]
print(country)

#country.clear()
#print(country)

print(len(country))

print(country.get("india"))

print(country.popitem())
print(country)

print(country.pop("england"))

country.update(italy= "paris")
print(country)

country.update(china= "beijing")
print(country)

country.update(italy= "rome")
print(country)

employees = [
    {"id": 1, "name": "Harsha", "role": "QA"},
    {"id": 2, "name": "Anil", "role": "Dev"},
    {"id": 3, "name": "Ravi", "role": "Manager"}
]

print(employees[0])
print(employees[0]["name"])

for emp in employees:
    if emp["name"] == "Harsha":
        print(emp)

employees.pop()
print(employees)


