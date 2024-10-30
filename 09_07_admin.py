# From Exercise 9-3
class User:
    def __init__(self, first_name, last_name, age, phone_number, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.location = location

    def describe_user(self):
        print(f"User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Phone number: {self.phone_number}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back!\n")

class Admin(User):
    def __init__(self, first_name, last_name, age, phone_number, location):
        super().__init__(first_name, last_name, age, phone_number, location)  # Call the parent class's constructor
        self.privileges = []  # Empty list for privileges

    def add_privilege(self, privilege):
        self.privileges.append(privilege)  # Method adds privilege to list

    def show_privileges(self):
        print(f"{self.first_name} {self.last_name}'s Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Instance of Admin
admin_user = Admin("Brin", "Finn", 23, "930-444-8329", "Venice CA")

# Privileges added
admin_user.add_privilege("can add post")
admin_user.add_privilege("can delete post")
admin_user.add_privilege("can ban user")

# Methods called to display user info and privileges
admin_user.describe_user()
admin_user.show_privileges()