print("=" * 60)
print("Python FUNDAMENTALS Prgrams")
print("=" * 60)

# Data Types
print("\n1. Data Types")
print("-" * 30)

name = "Mohd Umair"
age = 25
domain = "DevOps"
is_student = True
favorite_number = [10, 7, 11]
coordinates = (10, 20)

print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Domain: {domain}, Type: {domain}")
print(f"Student: {is_student}, Type: {type(is_student)}")
print(f"Favourite Number: {favorite_number}, Type: {type(favorite_number)}")
print(f"Coordinates: {coordinates}, Type: {type(coordinates)}")
print("-" * 30)

# Operators
print("\n\n2. Operators")
print("-" * 30)

a = 10
b = 7

# Arithmatic Operators
print(f"\nArithmatic Operators:")
print(f"a: {a}, b:{b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Substraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = { a / b}")
print(f"Floor Divison: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = { a % b}")
print(f"Exponent: {a} ** {b} = { a ** b}")
print("-" * 30)

# Comparison Operators
print(f"\nComparison Operators:")
print(f"{a} > {b} = {a > b}")
print(f"{a} < {b} = {a < b}")
print(f"{a} = {b} = {a == b}")
print(f"{a} != {b} = {a != b}")
print("-" * 30)

# String Operation
print("\n\n3. String Practice")
print("-" * 30)

text = "Hello! My name is Mohd Umair and I am a DevOps Engineer"
print(f"Original Text: {text}")
print(f"Length of text: {len(text)}")
print(f"Upper Case: {text.upper()}")
print(f"Upper Case: {text.lower()}")
print(f"Strip Case: {text.strip()}")
print(f"Replace: {text.replace('Umair','Hassan')}")

# String Slicing 
word = "Programming"
print(f"\nSclicing: {word}")
print(f"Slicing first 4: {word[0:4]}")
print(f"Slicing last 4: {word[-4:]}")
print(f"Middile letter: {word[2:8]}")
print(f"every 2nd letter: {word[::2]}")
print(f"Reverse: {word[::-2]}")

# String formatting
name1 = "Hassan Abbas"
score = 69
print(f"\nString Formatting: ")
print(f"f-string: {name1} scored {score}%")
print("format(): {} scored {:.1f}%".format(name1, score))
print("-" * 30)

# Grade Calculator function
def calculate_garde(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C" 
    elif score >= 60:
        return "D"
    else:
        return "F"
    
test_score = [80, 60, 25, 40, 20]
print("Garde Calculator")
for score in test_score:
    grade = calculate_garde(score)
    print(f" Score: {score}, --> grade: {grade}")

# Age calculator
def age_category(age):
    if age < 13:
        return "child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Buddha or Buddhi"
    else: 
        return "Upaar wala bulane wal hai isko"
    
print(f"Age Calculator")
age_list = [40, 90, 70, 20 , 15]
for age in age_list:
    catgory = age_category(age)
    print(f"Age: {age}, --> category: {catgory}")
print("=" * 30)