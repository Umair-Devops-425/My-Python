# Program to find a number enter by user is even or odd
n = int(input("Enter a number: "))

if n > 0:
    if n % 2 == 0:
        print("Yes! Its an even number")
    else:
        print("Number is Odd")
elif n == 0:
    print("Number you Enter is 0")
else:
    print("Number is negative integer")
