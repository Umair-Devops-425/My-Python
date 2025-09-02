# write a program to check a number is multiple of 7
n = int(input("Enter a number: "))

if n > 0:
    if n % 7 == 0:
        print("Yes! it's a multiple of 7")
    else:
        print("No! it's not a multiple of 7")
elif n == 0:
    print("The number you enter is: ",n)
else:
    print("The number you entered is negative integer")