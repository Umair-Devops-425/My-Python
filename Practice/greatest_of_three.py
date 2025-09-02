# write a program to find the greatest of 3 numbers entered by the user 
a = int(input("Enter a 1st number: "))
b = int(input("Enter a 2nd number: "))
c = int(input("Enter a 3rd number: "))

if a > b and a > c:
    print(a," is the greatest number")
elif b > c:
    print(b," is the greatest number")
else:
    print(c," is the greatest number")