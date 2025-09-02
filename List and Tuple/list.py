fruits = ['apple','banana','mango']

# printing list
print(fruits[0])

# adding a new element
fruits.append('dates')
print(fruits)

# adding at specific index
fruits.insert(1,'orange')
print(fruits)

# remove an element
fruits.remove('apple')
print(fruits)

# remove and return last element
pooped = fruits.pop()
print(pooped)

# Remove by index
del fruits[0]
print(fruits)

# Get Length
print(len(fruits))

# Sort in place
fruits.sort()

# Reverse in place
fruits.reverse()