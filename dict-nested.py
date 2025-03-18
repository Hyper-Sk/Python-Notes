cars = {
    'suzuki':{
        'model':'Swift Desire VDI',
        'colors':['red','white','black'],
        'miledge': 12,
    },
    'toyota':{
        'model':'Fortuner',
        'colors':['gray','white','black'],
        'miledge': 10,
    },
    'mahindra':{
        'model':'scorpio',
        'colors':['navyblue','white','black'],
        'miledge': 10,
    }
}


suzukiModel = cars['suzuki']['model']
print(suzukiModel)

toyotaColors = cars['toyota']['colors']
print(toyotaColors)



# add childs into the parent 

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 

print(myfamily['child1'])