class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size  # 40 is the default size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range_miles = 150
        elif self.battery_size == 65:
            range_miles = 225
        print(f"This car can go about {range_miles} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
        else:
            print("Battery is already at maximum capacity.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)  # Parent class constructor called
        self.battery = Battery()  # Instance of Battery made

# Instance of ElectricCar
my_leaf = ElectricCar('Nissan', 'Leaf', 2024)

# Car's description
print(my_leaf.get_descriptive_name())

# Battery description and range
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

my_leaf.battery.upgrade_battery()

# Range after upgrading the battery
my_leaf.battery.get_range()
