# Lists
friends = ["Cooper", "Kei", "Joel", "Jonny", "Zack"]
names = friends.copy()
numbers = [1, 2, 3, 4, 5]

print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[2:])
print(friends[1:3])
friends[1] = "Larissa"
print(friends)

# List Functions
friends.extend(numbers)
print(friends)
friends.append("Pete")
print(friends)
friends.remove("Zack")
print(friends)
friends.pop()
print(friends)
print(friends.index("Joel"))
print(names)
names.sort()
print(names)