items = [0, 1, 2, 3, 4, 5, 6]
print(items)

a = slice(2, 4)
print(items[2: 4])
print(items[a])

items[a] = [10,11]
print(items)

del items[a]
print(items)
