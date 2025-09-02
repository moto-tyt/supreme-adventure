class Dog:
    def __init__(self, name):
        # show object dictionary before adding attribute
        print("Before:", self.__dict__)
        self.name = name
        self.gate = Cat("T")
        # show object dictionary after adding attribute
        print("After:", self.__dict__)

class Cat:
    def __init__(self, name):
        self.name = name
        self.ddg = Dog("circular")
    
    def __repr__(self):
        return f"T: Cat"

# create Dog object
d = Dog("Rex")