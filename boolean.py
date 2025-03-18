# The following will return False:

print(bool(False))
print(bool(0))
print(bool(''))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(None))

# pyhton can return boolean /

def hello():
    return True
print(hello())


# check instance of any variable /

x = True 
print(isinstance(x, bool))