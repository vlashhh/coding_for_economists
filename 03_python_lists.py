myList = [1, 2, 3, 4, 5]

print(myList)

print(type(myList))

print(myList[0])


print(f'Our list object myList has {len(myList)} elements')

mixedList = [1, 'two', 3.0, [4, 'four'], 5]
print(mixedList)

mixedList.append(6)
print(mixedList)

mixedList.pop()
print(mixedList)

print(mixedList.count(1))

mixedList.reverse()
print(mixedList)