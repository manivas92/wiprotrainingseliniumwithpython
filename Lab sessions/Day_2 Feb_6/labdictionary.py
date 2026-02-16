
number ={ 1 : "mani", 2 :"sai", 3 :"abhi", 4: "varun",5:"kiran"}
print(number)

states = {}
print(states)

states.update( ap = "amaravati")
states.update( ts = "hyderabad")
states.update( tn = "chennai")
states.update( ka = "bengaluru")
states.update( ma  = "mumbai")
print(states)

print(states.get("ts"))

states.update(mp = "indore")
print(states)

states.pop("ma")
print(states)

print(len(number))

number.get(1)
print(number)

print(number.keys())

print(number.values())

print(number)
