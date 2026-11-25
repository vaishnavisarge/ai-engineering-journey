# An instance method is a function defined inside a class that operates on an 
# individual object's data.
# It takes self as its first parameter.

class PasswordChecker:

    def __init__(self, password):
        self.password = password

    def check_length(self):
        return len(self.password) >= 8

    def check_digit(self):
        return any(char.isdigit() for char in self.password)

    def check_uppercase(self):
        return any(char.isupper() for char in self.password)

    def check_strength(self):
        print("Length:", self.check_length())
        print("Contains digit:", self.check_digit())
        print("Contains uppercase:", self.check_uppercase())


p1 = PasswordChecker("Python@123")
p1.check_strength()