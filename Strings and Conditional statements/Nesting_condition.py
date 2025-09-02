name = input("Please Enter your name: ")
age = int(input("Please Enter Your age: "))
country = input("Please Enter Your country: ")

if country == "US":
    if age >= 20:
        print("Mr.", name, "You are eligible for voting")
    else:
        print("Mr.", name, "Ghar jaoo app apne")
else:
    print("Not availabe")