bike = {
    'name': 'yamaha',
    'miledge' : 35,
    'year': 1997,
    'color':'white',
    'dickBrake':True,
    'model':'rx100'
}

# remove the pair using key 
bike.pop('dickBrake')
print(bike)

# removes the last inserted pair 
bike.popitem()
print(bike)

# delete the pair using key with del 
del bike['year']
print(bike) 