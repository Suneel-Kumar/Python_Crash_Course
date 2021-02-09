class MyCar:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + self.model
        return long_name.title()
    def set_odometer_reading(self,mileage):
        self.odometer_reading = mileage
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")