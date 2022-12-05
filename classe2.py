"""
Classes
"""


class Car:
    def __init__(self, manufacturer, color, actual_mileage):
        self._manufacturer = None
        self._manufacturer = manufacturer
        self._color = color
        self._actual_mileage = actual_mileage

    """ Now we are going to declare getters and setters """

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self._manufacturer = manufacturer

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def actual_mileage(self):
        return self._actual_mileage

    @actual_mileage.setter
    def actual_mileage(self, actual_mileage):
        self._actual_mileage = actual_mileage

    def start_engine(self):
        return f"{self._manufacturer} start the motor"


car1 = Car("Volkswagen", "Blue", 1000)

# Get the Values
print(car1.manufacturer)
print(car1.color)
print(car1.actual_mileage)

# Set the values
car1.manufacturer = "NAMX"
car1.color = "White"
car1.actual_mileage = 4000
print()
print(car1.manufacturer)
print(car1.color)
print(car1.actual_mileage)
print(car1.start_engine())
print()

# Class methods: Class method are methods that we can access without needing to
# create any new object at all


class Website:
    url = "https://www.ccbremen.de"

    def __int__(self, navbar, content, footer):
        self.navbar = navbar
        self.content = content
        self.footer = footer

    @classmethod
    def get_url(cls):
        return cls.url


print(Website.get_url())
print()

""" 
Static methods: are utility functions that are supposed to help us do something
                with arguments that are passed when calling them.
                Static methos cannot modify class or instance attributes.
"""


class Website:
    url = "https://www.ccbremen.de"

    def __init__(self, navbar, content, footer):
        self.navbar = navbar
        self.content = content
        self.footer = footer

    @classmethod
    def get_url(cls):
        return cls.url

    @staticmethod
    def last_update(date):
        print(f'The last update was achieved on {date}')


website = Website(["Home", "About", "Contact"], "The content", "footer")
website.last_update("26.11.2022")
