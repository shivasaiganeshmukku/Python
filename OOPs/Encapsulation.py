'''🔹 Basic Encapsulation
- Create a Student class with private attributes name and marks.
-- Provide getter and setter methods to access and update them.
- Write a BankAccount class with private attributes balance.
-- Add methods deposit() and withdraw() that update balance safely.
- Implement a Car class with private attributes speed.
-- Add methods to increase/decrease speed but prevent negative values.

🔹 Intermediate Encapsulation
- Create an Employee class with private attributes salary.
-- Add a method to apply a raise but restrict direct modification of salary.
- Write a Product class with private attributes price and quantity.
-- Add methods to calculate total cost and update stock safely.
- Implement a User class with private attributes password.
-- Add methods to change password but prevent direct access.

🔹 Advanced Encapsulation
- Build a LibraryBook class with private attributes title, author, and availability.
-- Add methods to borrow/return books with proper checks.
- Create a Flight class with private attributes seats_available.
-- Add methods to book/cancel tickets ensuring seats don’t go negative.
- Implement a ShoppingCart class with private attributes items.
-- Add methods to add/remove items and calculate total cost.
- Write a SecureData class with private attributes and methods.
-- Demonstrate how encapsulation hides implementation details but exposes controlled access.

🎯 Simple Way to Understand Encapsulation
Think of it like a TV remote:
- You don’t directly touch the circuits inside the TV.
- You only use the buttons (methods) provided to interact with it.
- Encapsulation hides the internal complexity and gives you a safe interface.
'''

#- Create a Student class with private attributes name and marks.
class Student:
    def __init__(self, name, age):
        self.__name= name
        self.__age = age
# -- Provide getter and setter methods to access and update them.
    def get_student(self):
        print(self.__name)
        print(self.__age)
    def set_student(self,name , age):
        self.__name= name
        print(self.__name)
        self.__age = age
        print(self.__age)
student = Student("shiva", 21)
student.get_student()
student.set_student("sai", 22)

# - Write a BankAccount class with private attributes balance.
class BankAccount:
    def __init__(self, Balance):
        self.__Balance = Balance
# -- Add methods deposit() and withdraw() that update balance safely.
    def get_balance(self):
        print(f"Total balance: {self.__Balance}")
    def deposit(self ,amount):
        if amount > 0:
            self.__Balance += amount
            print(f"Deposited {amount}, new balance: {self.__Balance}")
        else:
            return "invalid amount"
    def withdraw(self, amount):
        if amount <= self.__Balance:
            self.__Balance -= amount
            print(f"Remaining balance: {self.__Balance}")
        else:
            print("Enter sufficient amount")
BA = BankAccount(1000)
BA.get_balance()
BA.deposit(500)
BA.withdraw(90)

# - Implement a Car class with private attributes speed.
class Car:
    def __init__(self, speed):
        self.__speed = speed
        print(self.__speed)
# -- Add methods to increase/decrease speed but prevent negative values.
    def increase_speed(self,  increase):
        self.increase = increase
        if increase > 0:
            self.__speed +=increase
            print(f"speed increased by {self.__speed}")
        else:
            print("same speed")
    def decrease_speed(self, amount):
        if amount > 0:
            if self.__speed - amount < 0:
                self.__speed = 0   # Prevent negative speed
            else:
                self.__speed -= amount
            print(f"Braked by {amount}. Current speed: {self.__speed}")
        else:
            print("Invalid brake amount")


c = Car(60)
c.increase_speed(10)
c.decrease_speed(60)

# 🔹 Intermediate Encapsulation
# - Create an Employee class with private attributes salary.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    def display(self):
        print(self.name)
        print(self.__salary)
    def get_salary(self):
        return self.__salary
# -- Add a method to apply a raise but restrict direct modification of salary.
    def  raise_salary(self , amount):
        if amount > 0:
            self.__salary += amount
            print(f"Increased salary {self.__salary}")
        else:
            print("salary not increased")
    
emp = Employee("shiva", 30000)
emp.display()
emp.raise_salary(10000)

# - Write a Product class with private attributes price and quantity.
class Product:
    def __init__(self, price, quantity):
        self.__price = price       # private attribute
        self.__quantity = quantity # private attribute

    # Getter methods
    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    # Method to calculate total cost
    def get_total_cost(self):
        return self.__price * self.__quantity

    # Method to update stock safely
    def update_stock(self, amount):
        # Adding stock
        if amount > 0:
            self.__quantity += amount
            print(f"Added {amount} units. New quantity: {self.__quantity}")
        # Removing stock
        elif amount < 0:
            if self.__quantity + amount >= 0:   # prevent negative stock
                self.__quantity += amount
                print(f"Removed {-amount} units. New quantity: {self.__quantity}")
            else:
                print("Error: Not enough stock to remove.")
        else:
            print("No change in stock.")

# Example usage
p = Product(100, 10)

print("Price per unit:", p.get_price())
print("Initial quantity:", p.get_quantity())
print("Total cost:", p.get_total_cost())

p.update_stock(5)    # Add stock
p.update_stock(-3)   # Remove stock
p.update_stock(-20)  # Attempt to remove too much
print("Final total cost:", p.get_total_cost())

# - Implement a User class with private attributes password.
# -- Add methods to change password but prevent direct access.
class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password   # private attribute

    # Method to change password safely
    def change_password(self, old_password, new_password):
        if self.__password == old_password:
            if new_password:   # ensure new password is not empty
                self.__password = new_password
                print("Password changed successfully.")
            else:
                print("New password cannot be empty.")
        else:
            print("Incorrect old password. Password not changed.")

    # Method to verify password (optional)
    def verify_password(self, pwd):
        return self.__password == pwd


# Example usage
user = User("shiva", "123456789")

# Try changing with correct old password
user.change_password("123456789", "newpass")

# Try changing with wrong old password
user.change_password("wrongpass", "anotherpass")

# Verify new password
print("Password correct?", user.verify_password("newpass"))

# 🔹 Advanced Encapsulation
# - Build a LibraryBook class with private attributes title, author, and availability.
# -- Add methods to borrow/return books with proper checks.
class LibraryBook:
    def __init__(self, title, author, availability):
        self.__title = title
        self.__author = author
        self.__availability = availability   # True = available, False = borrowed

    # Method to borrow a book
    def borrow(self):
        if self.__availability:
            self.__availability = False
            print(f"You borrowed '{self.__title}' by {self.__author}.")
        else:
            print(f"Sorry, '{self.__title}' is not available right now.")

    # Method to return a book
    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"You returned '{self.__title}'. Thank you!")
        else:
            print(f"'{self.__title}' was not borrowed.")

    # Getter to check availability
    def is_available(self):
        return self.__availability


# Example usage
lib = LibraryBook(" Your Life", "Anyan", True)

lib.borrow()          # Borrow the book
lib.borrow()          # Try borrowing again (not available)
lib.return_book()     # Return the book
lib.return_book()     # Try returning again (already available)

# - Create a Flight class with private attributes seats_available.
# -- Add methods to book/cancel tickets ensuring seats don’t go negative.
class Flight:
    def __init__(self, seats_available):
        self.__seats_available = seats_available   # private attribute

    # Method to book tickets
    def book(self, seats=1):
        if seats <= self.__seats_available:
            self.__seats_available -= seats
            print(f"Booked {seats} seat(s). Remaining seats: {self.__seats_available}")
        else:
            print("Not enough seats available.")

    # Method to cancel tickets
    def cancel_tickets(self, seats=1):
        if seats > 0:
            self.__seats_available += seats
            print(f"Cancelled {seats} seat(s). Available seats: {self.__seats_available}")
        else:
            print("Invalid cancellation request.")

    # Getter to check available seats
    def get_available_seats(self):
        return self.__seats_available


# Example usage
fly = Flight(5)   # Flight starts with 5 seats

fly.book(2)       # Book 2 seats
fly.book(4)       # Try booking 4 seats (not enough)
fly.cancel_tickets(1)  # Cancel 1 seat
print("Final available seats:", fly.get_available_seats())

# - Implement a ShoppingCart class with private attributes items.
# -- Add methods to add/remove items and calculate total cost.
class ShoppingCart:
    def __init__(self,items,cost):
        self.cost= cost
        self.__items = items
        
    def add_items(self, item):
        if self.__items:
            self.__items += item
            print(f"added items are {self.__items}")
        else:
            print(self.__items)
        
    def remove_items(self, rem):
        if rem:
            self.__items -=rem
            print(f"removed items {self.__items}")
        else:
            print("items are not removed")
    def get_total_items_cost(self):
        print(f"total cost of the items. Items{self.__items} cost{self.cost}")
        print(f"cost of items are {self.cost * self.__items}")
        return self.__items
shp = ShoppingCart(4 ,50)
shp.add_items(1)
shp.remove_items(2)
shp.get_total_items_cost()

class ShoppingCart:
    def __init__(self):
        # Store items as a dictionary: {item_name: price}
        self.__items = {}

    def add_item(self, item, price):
        self.__items[item] = price
        print(f"Added {item} with price {price}")

    def remove_item(self, item):
        if item in self.__items:
            del self.__items[item]
            print(f"Removed {item}")
        else:
            print(f"{item} not found in cart")

    def get_total_cost(self):
        total = sum(self.__items.values())
        print(f"Total cost of items: {total}")
        return total

    def show_items(self):
        print("Items in cart:", self.__items)

cart = ShoppingCart()
cart.add_item("Apple", 50)
cart.add_item("Banana", 20)
cart.show_items()
cart.remove_item("Apple")
cart.get_total_cost()

# - Write a SecureData class with private attributes and methods.
# -- Demonstrate how encapsulation hides implementation details but exposes controlled access.
class SecureData:
    def __init__(self, password):
        self.__password = password
        self.__data = None
    # private methods
    def __encrypt(self, data):
        return "".join(chr(ord(c) + 1) for c in data)  # simple shift cipher
    def __decrypt(self,data):
        return "".join(chr(ord(c) - 1) for c in data)
    # Public method to store data
    def store_data(self, data , password):
        if password == self.__password:
            self.__data = self.__encrypt(data)
            print("Data stored securely.")
        else:
            print("Access denied. Wrong password.")
    # Public method to retrieve data
    def retrieve_data(self, password):
        if password == self.__password and self.__data:
            return self.__decrypt(self.__data)
        else:
            return "Access denied or no data stored."
secure = SecureData("my password")

secure.store_data("Hello World", "my password")   # stores securely
print(secure.retrieve_data("my password"))       # retrieves original data
print(secure.retrieve_data("wrong pass"))        # denied