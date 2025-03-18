# assigning random key and value '
# it will check and append that value.

bike = {
    'name': 'yamaha',
    'miledge' : 35,
    'year': 1997,
    'color':'white'
}

bike['model'] = 'rx100'
print(bike)

bike.update({'discBrake': 1})
print(bike)

