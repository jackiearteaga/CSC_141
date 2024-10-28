class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def added_number_served(self, number):
        self.number_served += number

# Instance
restaurant = Restaurant("MyThai", "Thai food")

# Number of customers served
print(f"Number of customers served: {restaurant.number_served}")

# Change number served
restaurant.set_number_served(25)
print(f"Number of customers served after update: {restaurant.number_served}")

restaurant.added_number_served(19)
print(f"Number of customers served after the addition: {restaurant.number_served}")

# Methods called
restaurant.describe_restaurant()
restaurant.open_restaurant()