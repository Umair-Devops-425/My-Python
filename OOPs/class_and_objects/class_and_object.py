# Define a class
class Dog:
    def __init__(self, name, colour, eye_colour, height, length):
        self.name = name
        self.colour = colour
        self.eye_colour = eye_colour
        self.height = height
        self.length = length
    
    # Methods
    def getName(self):
        return self.name
    
    def getColour(self):
        return self.colour
    
    def getEyeColour(self):
        return self.eye_colour
    
    def getHeight(self):
        return self.height
    
    def comeHere(self):
        return f"{self.name} is coming!"

# Create an object (instance)
tommy = Dog("Tommy", "Green", "Brown", "17in", "35in")

# Access properties and methods
print(tommy.getName())       # Tommy
print(tommy.getColour())     # Green
print(tommy.comeHere())      # Tommy is coming!
