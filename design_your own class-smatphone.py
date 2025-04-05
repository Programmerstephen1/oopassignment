# Class representing a Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    # Method to display information about the smartphone
    def display_info(self):
        print(f"Smartphone Info: {self.brand} {self.model} - ${self.price}")

    # Method to make a call
    def make_call(self, number):
        print(f"Calling {number}...")
        
    # Method to take a picture
    def take_picture(self):
        print("Picture taken!")
    
# Inheritance: MobilePhone (a specific type of Smartphone)
class MobilePhone(Smartphone):
    def __init__(self, brand, model, price, sim_slots):
        super().__init__(brand, model, price)
        self.sim_slots = sim_slots

    # Overriding the display_info method to include sim slots
    def display_info(self):
        print(f"MobilePhone Info: {self.brand} {self.model} - ${self.price}, SIM slots: {self.sim_slots}")
    
    # Overriding the make_call method for MobilePhone
    def make_call(self, number):
        print(f"Making call from {self.model} to {number}...")

# Creating an instance of Smartphone
phone = Smartphone("Apple", "iPhone 13", 999)
phone.display_info()
phone.make_call("123-456-7890")

# Creating an instance of MobilePhone (subclass of Smartphone)
mobile = MobilePhone("Samsung", "Galaxy S21", 799, 2)
mobile.display_info()
mobile.make_call("987-654-3210")
