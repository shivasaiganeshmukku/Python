'''🔹 Basic Polymorphism
- Create a base class Animal with a method sound().
- Derive Dog and Cat classes that override sound().
- Demonstrate calling sound() on different objects.0
0- Write a Shape base class with a method area().
- Derive Circle and Rectangle classes that implement their own area() methods.
0- Implement a Vehicle class with a method move().
- Subclasses: Car, Bike, Boat.
- Show how the same method name behaves differently.

🔹 Intermediate Polymorphism
- Create a Payment base class with a method pay().
- Subclasses: CreditCard, PayPal, UPI.
- Demonstrate polymorphism by calling pay() on different objects.
0- Write a program where a Bird class has a method fly().
- Subclasses: Sparrow, Penguin.
- Show how polymorphism handles different behaviors (flying vs. not flying).
0- Implement a Calculator class with a method operation(a, b).
- Subclasses: Adder, Multiplier, Divider.
- Demonstrate polymorphism with different operations.

🔹 Advanced Polymorphism
- Create a Employee base class with a method work().
- Subclasses: Manager, Developer, Intern.
- Demonstrate polymorphism by iterating over a list of employees and calling work().
0- Implement a MediaPlayer base class with a method play().
- Subclasses: AudioPlayer, VideoPlayer, StreamingPlayer.
- Show polymorphism in action.
0- Build a University system:
- Base class: Person with method role().
- Subclasses: Student, Professor, Staff.
- Demonstrate polymorphism by calling role() on different objects.
0- Write a program to demonstrate duck typing:
- Create two unrelated classes (Dog and Robot) both with a method walk().
- Write a function that accepts any object and calls walk().
- Show how polymorphism works without inheritance.

👉 Simple way to understand polymorphism:
Think of it like one word, many meanings. For example, the word “run” can mean:
- Run a race (athlete)
- Run a program (computer)
- Run a company (manager)
Same word, different behavior — that’s polymorphism in OOP.
'''
# Basic Polymorphism Example
# - Create a base class Animal with a method sound().
# - Derive Dog and Cat classes that override sound().
# - Demonstrate calling sound() on different objects.

class Animal:
    def sound():
        return "Animal sounds"
class Dog(Animal):
    def sound():
        return "Dog barks"
class Cat(Animal):
    def sound():
        return "cat sounds meow"
animals = [Animal,Dog, Cat]
for animal in animals:
    print(animal.sound())

# - Write a Shape base class with a method area().
# - Derive Circle and Rectangle classes that implement their own area() methods.
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of Circle: { 3.14 * self.radius ** 2}")
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(f"Area Rectangle : {self.width * self.height}")
    
shapes = [Circle(5), Rectangle(4,6)]
for shape in shapes:
    shape.area()

#  Implement a Vehicle class with a method move().
# - Subclasses: Car, Bike, Boat.
# - Show how the same method name behaves differently.
class Vehicle:
    def move(self):
        pass
class Car(Vehicle):
    def move(self):
        print("car is moving on road")
class Bike(Vehicle):
    def move(self):
        print("bike is moving on road")
class Boat(Vehicle):
    def move (self):
        print("Boat is moving on water")

vehicle = [Car(), Bike(), Boat()]
for v in vehicle:
    v.move()

    # 🔹 Intermediate Polymorphism
# - Create a Payment base class with a method pay().
# - Subclasses: CreditCard, PayPal, UPI.
# - Demonstrate polymorphism by calling pay() on different objects.
class Payment:
    def pay(self):
        pass
class CreditCard(Payment):
    def pay(self):
        print("Payment made using Credit card")
class Paypal(Payment):
    def pay(self):
        print("Payment made using PayPal")
class UPI(Payment):
    def pay(self):
        print("Payment made using UPI")
payments = [CreditCard(), Paypal(), UPI()]
for p in payments:
    p.pay()

    # - Write a program where a Bird class has a method fly().
# - Subclasses: Sparrow, Penguin.
# - Show how polymorphism handles different behaviors (flying vs. not flying).
class Bird:
    def fly(self):
        pass
class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly")
class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")
birds = [Sparrow(), Penguin()]
for bird in birds:
    bird.fly()

# - Implement a Calculator class with a method operation(a, b).
# - Subclasses: Adder, Multiplier, Divider.
# - Demonstrate polymorphism with different operations.
# Base class
class Calculator:
    def operation(self, a, b):
        raise NotImplementedError("Subclass must implement this method")


# Subclass for addition
class Adder(Calculator):
    def operation(self, a, b):
        return a + b


# Subclass for multiplication
class Multiplier(Calculator):
    def operation(self, a, b):
        return a * b


# Subclass for division
class Divider(Calculator):
    def operation(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b


# Demonstration of polymorphism
def perform_operation(calculator_obj, a, b):
    print(f"Result: {calculator_obj.operation(a, b)}")


# Example usage
add = Adder()
multi = Multiplier()
div = Divider()

perform_operation(add, 10, 5)        # Addition
perform_operation(multi, 10, 5)   # Multiplication
perform_operation(div, 10, 5)      # Division

# 🔹 Advanced Polymorphism
# - Create a Employee base class with a method work().
# - Subclasses: Manager, Developer, Intern.
# - Demonstrate polymorphism by iterating over a list of employees and calling work().

#Base class
class Employee:
    def work(self):
        return 'working'
class Manager(Employee):
    def work(self):
        return "managing"
class Developer(Employee):
    def work(self):
        return "developing"
class Intern(Employee):
    def work(self):
        return "learning"
    
boom = [Manager(),Developer(),Intern()]
for i in boom:
    print(i.work())

# Implement a MediaPlayer base class with a method play().
# - Subclasses: AudioPlayer, VideoPlayer, StreamingPlayer.
# - Show polymorphism in action.

#Base class
class MediaPlayer:
    def play(self):
        return "Started Playing"
class AudioPlayer(MediaPlayer):
    def play(self):
        return "AudioPlayer is playing"
class VideoPlayer(MediaPlayer):
    def play(self):
        return "VideoPlayer is playing"
class StreamingPlayer(MediaPlayer):
    def play(self):
        return "StreamingPlayer is streaming"
    
player = [AudioPlayer(),VideoPlayer(),StreamingPlayer()]
for i in player:
    print(i.play())

# Build a University system:
# - Base class: Person with method role().
# - Subclasses: Student, Professor, Staff.
# - Demonstrate polymorphism by calling role() on different objects.

class Person:
    def role(self):
        return "role of the person:"
    
class Student(Person):
    def role(self):
        return "Student"
class Professor(Person):
    def role(self):
        return "professor"
class Staff(Person):
    def role(self):
        return "staff"
r = Person()
print(r.role())
s = Student()
print(s.role())
p = Professor()
print(p.role())
st= Staff()
print(st.role())

# Write a program to demonstrate duck typing:
# - Create two unrelated classes (Dog and Robot) both with a method walk().
# - Write a function that accepts any object and calls walk().
# - Show how polymorphism works without inheritance.
class Dog:
    def walk(self):
        return "Dog walking"
class Robot:
    def walk(self):
        return "Robot is walking"
    
def walking(w ):
    print(w.walk())

dog = Dog()
robot = Robot()
print(dog.walk())
print(robot.walk())