bike = {
    'name': 'yamaha',
    'miledge' : 35,
    'year': 1997,
    'color':'white',
    'dickBrake':True,
    'model':'rx100'
}


# only prints the keys 
for x in bike:
    print(x)

print("-------------------")

# only prints the values 
for y in bike.values():
    print(y)

print("-------------------")

# only prints the keys 
for z in bike.keys():
    print(z)

print("-------------------")

# prints the key and value 
for a,b in bike.items():
    print(a,b)

print("-------------------")
