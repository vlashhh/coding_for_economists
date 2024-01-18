mySet = {1, 2, 3}

print(mySet)

print(type(mySet))

# Sets contains only unique values

mySet = {1, 2, 3, 3}
print(mySet) # Last element removed authomatically

print(1 in mySet)

print(set('aaaaabbbbbbcccccc'))

setA = {1, 2, 3}

listB = [3, 4, 5, 5, 5, 5,5,5,5,5,5,5]
setB = set(listB)

print(setA, setB)

unionAB = setA | setB
print(unionAB)

intersecAB = setA & setB
print(intersecAB)