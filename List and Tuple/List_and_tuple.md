# Lists in Python
Lists are ordered collections that are mutable (can be changed after creation).

- Creating Lists:
```
# Empty list
my_list = []

# List with values
fruits = ['apple', 'banana', 'orange']
numbers = [1, 2, 3, 4, 5]
mixed = ['hello', 42, 3.14, True]  # Can store different data types
```

- Common List Operations:
```
fruits = ['apple', 'banana', 'orange']

# Accessing elements (0-based indexing)
print(fruits[0])    # 'apple'
print(fruits[-1])   # 'orange' (negative indexing from end)

# Adding elements
fruits.append('grape')        # Add to end
fruits.insert(1, 'mango')    # Insert at specific position

# Removing elements
fruits.remove('banana')       # Remove by value
popped = fruits.pop()         # Remove and return last element
del fruits[0]                 # Remove by index

# Other useful methods
print(len(fruits))           # Get length
fruits.sort()                # Sort in place
fruits.reverse()             # Reverse in place
```

# Tuples in Python
Tuples are ordered collections that are immutable (cannot be changed after creation).

- Creating Tuples:
```
# Empty tuple
empty_tuple = ()

# Tuple with values
coordinates = (10, 20)
colors = ('red', 'green', 'blue')
mixed_tuple = ('hello', 42, 3.14)

# Single element tuple (note the comma!)
single = (42,)  # or single = 42,
```

## When to Use Which?
- Use Lists when:
    - You need to add, remove, or modify elements
    - Working with data that changes over time
    - Need methods like `append()`, `remove()`, `sort()`

- Use Tuples when:
    - Data should remain constant (like coordinates, RGB values)
    - Need better performance
    - Want to use as dictionary keys (tuples can be keys, lists cannot)
    - Returning multiple values from a function