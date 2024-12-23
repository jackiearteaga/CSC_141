class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Instance
restaurant = Restaurant("MyThai", "Thai food")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Calling the methods
restaurant.describe_restaurant()
restaurant.open_restaurant()