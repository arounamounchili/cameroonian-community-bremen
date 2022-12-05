"""
Inheritance: Inheritance allows us to define a class that inherits all the
             methods and properties from another class.
             Parent class (base class) is the class being inherited from.
             Child class (derived class) is the class that inherits from another class
"""


# Create a Parent Class
class Vehicle:
    def __init__(self, name, number_of_wheels):
        self.name = name
        self.number_of_wheels = number_of_wheels

    def __str__(self):
        return f"{self.name} with {self.number_of_wheels} wheels\n"


# Create an object
vehicle1 = Vehicle("Mercedes", 4)
print(vehicle1)


# Create a Child Class
class Car(Vehicle):
    pass


car1 = Car("VW", 4)
print(car1)


#
class Bike(Vehicle):
    # When you add the __init__() function, the child class will no longer
    # inherit the parent's __init__ function
    def __init__(self, name, number_of_wheels, is_electric):
        # Use the super() function that will make the child inherit all
        # properties and methods from its parent
        super().__init__(name, number_of_wheels)
        self.is_electric = is_electric
        self.battery_level = None

        self.init_battery_level()

    def __str__(self):  # this override the the __str__() method in the parent class
        return f"{self.name} with {self.number_of_wheels} wheels and " \
               f"the Battery level is {self.battery_level}\n"

    def init_battery_level(self):
        if self.is_electric:
            self.battery_level = 100


e_bike = Bike(name="Velonix", number_of_wheels=2, is_electric=True)
print(e_bike)
print(f"The battery level is : {e_bike.battery_level}")

normal_bike = Bike("city Bike", 2, False)
print(normal_bike)
print(f"The battery level is : {normal_bike.battery_level}")


