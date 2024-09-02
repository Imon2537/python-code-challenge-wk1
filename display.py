# this function creates a class that prints out a cars information
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information: {self.year}, {self.make}, {self.model}")
        
obj1 = Car(2002, "corona", "brandy")
obj1.display_info()