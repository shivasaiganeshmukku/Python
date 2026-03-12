'''🔹 Beginner Level (Simple Demonstration)
Problem:
Create a BankAccount class that demonstrates encapsulation.
- Make balance a private attribute.
- Provide methods deposit() and withdraw() to safely update balance.
- Show how direct access to balance is restricted.
🔹 Intermediate Level (Combining Concepts)
Problem:
Build a Shape hierarchy to demonstrate abstraction + inheritance + polymorphism.
- Create an abstract class Shape with abstract method area().
- Derive Circle and Rectangle classes that implement area().
- Write a function that takes a list of shapes and prints their areas (polymorphism).
👉 This combines abstraction (abstract class), inheritance (subclasses), and polymorphism (same method behaves differently).

🔹 Advanced Level (Full Integration of All Four Pillars)
Problem:
Design a University Management System using all four pillars:
- Encapsulation: Keep student details (name, marks, ID) private with getters/setters.
- Abstraction: Create an abstract class Person with abstract method role().
- Inheritance: Derive Student, Professor, and Staff classes from Person.
- Polymorphism: Override role() in each subclass to display different roles.
👉 This project forces you to use all four pillars together in a real-world scenario.

🎯 Simple way to remember the four pillars:
- Encapsulation: Hide the data, expose safe methods.
- Abstraction: Define what must be done, not how.
- Inheritance: Reuse and extend existing code.
- Polymorphism: One interface, many implementations.
'''
# Problem:
# Create a BankAccount class that demonstrates encapsulation.
# - Make balance a private attribute.
# - Provide methods deposit() and withdraw() to safely update balance.
# - Show how direct access to balance is restricted.

class BankAccount():
    def __init__(self, balance ):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"deposit amount {amount}. total balance{self.__balance}")
        else:
            print("amount not be negative")
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"withdraw amount {amount}. remaining balance {self.__balance}")
        else:
            print(f"insufficient amount")

ba = BankAccount(5000)
ba.deposit(500)
ba.withdraw(1000)

# 🔹 Intermediate Level (Combining Concepts)
# Problem:
# Build a Shape hierarchy to demonstrate abstraction + inheritance + polymorphism.
# - Create an abstract class Shape with abstract method area().
# - Derive Circle and Rectangle classes that implement area().
# - Write a function that takes a list of shapes and prints their areas (polymorphism).

from abc import ABC , abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi*self.radius**2

class Rectangle(Shape):
        def __init__(self, length , height):
            self.length = length
            self.height = height
        def area(self):
            return self.length * self.height
        
def print_area(shape):
    for s in shape:
        print(f"{s.__class__.__name__} area: {s.area()}")
s = [Circle(3),Rectangle(4,5)]
print_area(s)


# 🔹 Advanced Level (Full Integration of All Four Pillars)
# Problem:
# Design a University Management System using all four pillars:
# - Encapsulation: Keep student details (name, marks, ID) private with getters/setters.
# - Abstraction: Create an abstract class Person with abstract method role().
# - Inheritance: Derive Student, Professor, and Staff classes from Person.
# - Polymorphism: Override role() in each subclass to display different roles.
from abc import ABC, abstractmethod

# Abstract Class (Abstraction)
class Person(ABC):
    def __init__(self, name, pid):
        self.name = name
        self.pid = pid

    @abstractmethod
    def role(self):
        pass


# Student Class (Inheritance + Encapsulation)
class Student(Person):
    def __init__(self, name, pid, marks):
        super().__init__(name, pid)
        self.__marks = marks   # private attribute

    # Getter
    def get_marks(self):
        return self.__marks

    # Setter
    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")

    # Polymorphism
    def role(self):
        print(f"{self.name} is a Student")


# Professor Class
class Professor(Person):
    def __init__(self, name, pid, subject):
        super().__init__(name, pid)
        self.subject = subject

    def role(self):
        print(f"{self.name} is a Professor teaching {self.subject}")


# Staff Class
class Staff(Person):
    def __init__(self, name, pid, department):
        super().__init__(name, pid)
        self.department = department

    def role(self):
        print(f"{self.name} works in {self.department} department")


# Main Program
s1 = Student("Ganesh", 677, 85)
p1 = Professor("Ram", 659, "Computer Science")
st1 = Staff("Suresh", 301, "Administration")

# Polymorphism demonstration
people = [s1, p1, st1]

for person in people:
    person.role()

# Encapsulation example
print("Student Marks:", s1.get_marks())
s1.set_marks(90)
print("Updated Marks:", s1.get_marks())

# 🔹 Problem: Library Management System
# Requirements
# - Encapsulation
# - Keep book details (title, author, ISBN, availability) private.
# - Provide getters/setters to safely access or update these values.
# - Abstraction
# - Create an abstract class LibraryItem with an abstract method display_info().
# - This ensures every item in the library must be able to show its details.
# - Inheritance
# - Derive Book, Magazine, and DVD classes from LibraryItem.
# - Each has its own attributes (e.g., Book has pages, DVD has duration).
# - Polymorphism
# - Override display_info() in each subclass to show details differently.
# - Write a function that takes a list of library items and prints their info, demonstrating polymorphism.


from abc import ABC, abstractmethod


# Abstraction

class LibraryItem(ABC):

    def __init__(self, title, author, isbn, availability=True):
        # Encapsulation (private variables)
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__availability = availability

    # Getters
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def is_available(self):
        return self.__availability

    # Setters
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_availability(self, status):
        self.__availability = status

    # Abstract method
    @abstractmethod
    def display_info(self):
        pass



# Inheritance - Book

class Book(LibraryItem):

    def __init__(self, title, author, isbn, pages):
        super().__init__(title, author, isbn)
        self.pages = pages

    # Polymorphism
    def display_info(self):
        print(f"Book: {self.get_title()} | Author: {self.get_author()} | "
              f"ISBN: {self.get_isbn()} | Pages: {self.pages} | "
              f"Available: {self.is_available()}")


# Inheritance - Magazine

class Magazine(LibraryItem):

    def __init__(self, title, author, isbn, issue_number):
        super().__init__(title, author, isbn)
        self.issue_number = issue_number

    def display_info(self):
        print(f"Magazine: {self.get_title()} | Editor: {self.get_author()} | "
              f"ISBN: {self.get_isbn()} | Issue No: {self.issue_number} | "
              f"Available: {self.is_available()}")


# Inheritance - DVD

class DVD(LibraryItem):

    def __init__(self, title, author, isbn, duration):
        super().__init__(title, author, isbn)
        self.duration = duration

    def display_info(self):
        print(f"DVD: {self.get_title()} | Director: {self.get_author()} | "
              f"ISBN: {self.get_isbn()} | Duration: {self.duration} mins | "
              f"Available: {self.is_available()}")



# Polymorphism Function

def print_library_items(items):
    for item in items:
        item.display_info()



# Main Program

b1 = Book("Python Programming", "John Smith", "ISBN101", 350)
m1 = Magazine("Tech Today", "Alice Brown", "ISBN202", 15)
d1 = DVD("AI Documentary", "David Lee", "ISBN303", 120)

library_items = [b1, m1, d1]

print_library_items(library_items)