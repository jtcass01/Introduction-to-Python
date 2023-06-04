# Class Example 2
class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year, cost, initial_reading = 0):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.cost = cost
        self.odometer_reading = initial_reading

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = '$' + str(self.cost) + " - " + \
            str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
# Create a new car
my_new_car = Car('ford', 'mach-e', 2021, 50000)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Create a car with a different default odometer reading
jacobs_car = Car('toyota', 'celica', 2000, 3000, initial_reading=230000)
print(jacobs_car.get_descriptive_name())
jacobs_car.read_odometer()

# Update odometer reading an re-read.
jacobs_car.odometer_reading = 12
jacobs_car.read_odometer()
