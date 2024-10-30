class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)  # Call the parent class's constructor
        self.flavors = []  # Empty list for flavors

    def add_flavor(self, flavor):
        self.flavors.append(flavor)  # Add a flavor to the list

    def display_flavors(self):
        print("Ice Cream Flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")  # Each flavor printed

# Instance of IceCreamStand
ice_cream_stand = IceCreamStand("Tasty Treats", "Divine Desserts")

# Added flavors
ice_cream_stand.add_flavor("Vanilla")
ice_cream_stand.add_flavor("Mint Chocolate Chip")
ice_cream_stand.add_flavor("Strawberry")

ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
ice_cream_stand.display_flavors()