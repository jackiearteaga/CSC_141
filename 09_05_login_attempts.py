class User:
    def __init__(self, first_name, last_name, age, phone_number, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.location = location
        self.login_attempts = 0  # Tracks login attempts

    def describe_user(self):
        print(f"User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Phone number: {self.phone_number}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1 

    def reset_login_attempts(self):
        self.login_attempts = 0 


# Several instances of User
user1 = User("Janice", "Ford", 62, "888-321-2321", "Philadelphia")
user2 = User("Shawn", "Mills", 30, "535-214-9760", "Portland")
user3 = User("Forest", "Scott", 22, "743-345-5903", "San Francisco")

# Methods
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

# Testing login attempts
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"{user1.first_name} {user1.last_name} has made {user1.login_attempts} login attempts.")

user1.reset_login_attempts()
print(f"After reset, {user1.first_name} {user1.last_name} has made {user1.login_attempts} login attempts.")