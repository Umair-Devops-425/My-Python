# what are strings
strings are sequences of characters used to represent text.

## How to create strings
- Single quotes:
`
'Hello'
`

- Double quotes:
`
"Hello"
`

- Triple quotes (single or double) for multi-line text:
`
'''This is a multi-line string.'''
`

## Key Properties of Strings
- They are sequences
You can access characters by index:
`
word = "Python"
print(word[0])  # P
print(word[-1]) # n
`

- They are immutable
Once created, you can’t change a string’s characters directly:
`
text = "cat"
text[0] = "b"  # ❌ Error
text = "bat"     # ✅ Create a new string
`

- They support operations
    - Concatenation (+): "Hello" + " World" → "Hello World"
    - Repetition (*): "Hi! " * 3 → "Hi! Hi! Hi! "
    - Slicing:
    `
    "Python"[0:3]  # 'Pyt'
    `

## String Functions
str = `"my name is umair"`
- str.endswith("er.")       # return true if strings end with substr
- str.capitalize()          # capatalize 1st char
- str.replace(old,new)      # replace all occurance of old with new
- str.find(word)            # return 1st index of 1st occurrerance
- str.count("am")           # counts the occurance of substr