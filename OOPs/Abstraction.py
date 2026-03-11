'''Basic Abstraction
- Create an abstract class Shape with an abstract method area().
- Derive Circle and Rectangle classes that implement area().
- Write an abstract class Animal with an abstract method sound().
- Implement subclasses Dog and Cat that override sound().
- Build an abstract class Vehicle with abstract methods start() and stop().
- Implement subclasses Car and Bike.

🔹 Intermediate Abstraction
- Create an abstract class Payment with abstract method pay(amount).
- Implement subclasses CreditCardPayment, PayPalPayment, and UPIPayment.
- Write an abstract class Employee with abstract method calculate_salary().
- Implement subclasses Manager and Developer with different salary rules.
- Build an abstract class Appliance with abstract methods turn_on() and turn_off().
- Implement subclasses Fan and Light.

🔹 Advanced Abstraction
- Create an abstract class Database with abstract methods connect(), disconnect(), and execute_query().
- Implement subclasses MySQLDatabase and MongoDatabase.
- Write an abstract class MediaPlayer with abstract methods play(), pause(), and stop().
- Implement subclasses AudioPlayer and VideoPlayer.
- Build an abstract class Account with abstract methods deposit(), withdraw(), and get_balance().
- Implement subclasses SavingsAccount and CurrentAccount.
- Create an abstract class Shape3D with abstract methods volume() and surface_area().
- Implement subclasses Cube and Sphere.

🎯 Simple Way to Understand Abstraction
Think of abstraction like driving a car:
- You only know how to use the steering wheel, accelerator, and brakes.
- You don’t need to know how the engine or transmission works internally.
- The abstract class defines the “interface” (what must exist), while subclasses define the “implementation” (how it works).
'''
#   Basic Abstraction
# - Create an abstract class Shape with an abstract method area().
# - Derive Circle and Rectangle classes that implement area().
from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self. r = r
    def area(self):
        print(f"Area of circle: {3.14*self.r**2}")
class Rectangle:
    def __init__(self, length , breath):
        self.length = length
        self.breath = breath
    def area(self):
        print(f"Area of Rectangle: {self.length * self.breath}")
    
c = Circle(3)
c.area()
r = Rectangle(4,5)
r.area()

# Write an abstract class Animal with an abstract method sound().
# - Implement subclasses Dog and Cat that override sound().
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("dog barks")
class Cat(Animal):
    def sound (self):
        print("Cat sounds meow")

d = Dog()
d.sound()
c = Cat()
c.sound()

# - Build an abstract class Vehicle with abstract methods start() and stop().
# - Implement subclasses Car and Bike.
from abc import ABC , abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("car start with the touch the start button")
    def stop(self):
        print("engine is stopped")
class Bike(Vehicle):
    def start(self):
        print("bike starts with a key and self-start")
    def stop(self):
        print("bike stops with a key or kill switch")
vehicle = [Car(), Bike()]
for v in vehicle:
    v.start()
    v.stop()

    # 🔹 Intermediate Abstraction
# - Create an abstract class Payment with abstract method pay(amount).
# - Implement subclasses CreditCardPayment, PayPalPayment, and UPIPayment.
from abc import ABC , abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay (self, amount):
        pass
class CreditCardPayment(Payment):
    def pay(self,amount):
        print(f"Payment done by the Credit Card Payment. {amount}")
class PayPalPayment(Payment):
    def pay (self,amount):
        print(f"Payment done by the Pay Pal payment. {amount}")
class UPIPayment(Payment):
    def pay(self,amount):
        print(f"Payment done by the UPIPayment {amount}")

payment = [CreditCardPayment(),PayPalPayment(),UPIPayment()]
amount = [100,500,1000]
for p,a in zip(payment,amount):
    p.pay(a)

    # - Write an abstract class Employee with abstract method calculate_salary().
# - Implement subclasses Manager and Developer with different salary rules.
from abc import ABC , abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class Manager(Employee):
    def __init__(self, base_salary , bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        print(f"Manager base salary:{self.base_salary}")
        print(f"bonus salary: {self.bonus}")
        print(f"Manager salary :{self.base_salary + self.bonus}")
class Developer(Employee):
    def __init__(self, base_salary, overtime_hour, overtime_rate):
        self.base_salary = base_salary
        self.overtime_hour = overtime_hour
        self.overtime_rate = overtime_rate

    def calculate_salary(self):
        print(f"Developer base_salary: {self.base_salary}")
        print(f"over time worked hours : {self.overtime_hour}")
        print(f"over time rate : {self.overtime_rate}")
        print(f"total salary of Developer : {self.base_salary+(self.overtime_hour*self.overtime_rate)}")
        
m = Manager(50000, 10000)
m.calculate_salary()
d = Developer(40000,10,500)
d.calculate_salary()

# - Build an abstract class Appliance with abstract methods turn_on() and turn_off().
# - Implement subclasses Fan and Light.
from abc import ABC, abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
class Fan(Appliance):
    def turn_on(self):
        print("turn on the fan switch it running")
    def turn_off(self):
        print("turn off the fan switch to off the fan")
class Light(Appliance):
    def turn_on(self):
        print("Lights on")
    def turn_off(self):
        print("Lights off")
appliance = [Fan(), Light()]
for a in appliance:
    a.turn_on()
    a.turn_off()

    # 🔹 Advanced Abstraction
# - Create an abstract class Database with abstract methods connect(), disconnect(), and execute_query().
# - Implement subclasses MySQLDatabase and MongoDatabase.
from abc import ABC , abstractmethod
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
    @abstractmethod
    def execute_query(self):
        pass
class MySQLDatabase(Database):
    def connect(self):
        print("connected to MySQLDatabase")
    def disconnect(self):
        print("disconnected MySQLDatabase ")

    def execute_query(self):
        print("query executed MySQLDatabase")
class MongoDatabase(Database):
    def connect(self):
        print("connected to the MongoDatabase")
    def disconnect(self):
        print("disconnected to the MongoDatabase")
    def execute_query(self):
        print("executed query MongoDatabase")

db = [MySQLDatabase(),MongoDatabase()]
for D in db:
    D.connect()
    D.disconnect()
    D.execute_query()



# - Write an abstract class MediaPlayer with abstract methods play(), pause(), and stop().
# - Implement subclasses AudioPlayer and VideoPlayer.
from abc import ABC , abstractmethod
class MediaPlayer(ABC):
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def pause(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class AudioPlayer(MediaPlayer):
    def play(self):
        print("Audio is playing")

    def pause(self):
        print("Audio is paused")
    def stop(self):
        print("Audio is stop")

class VideoPlayer(MediaPlayer):
    def play(self):
        print("Video player is playing the video")
    def pause(self):
        print("Video player is paused the video ")
    def stop(self):
        print("Video player is stop the video.")

A = AudioPlayer()
A.play()
A.pause()
A.stop()
V = VideoPlayer()
V.play()
V.pause()
V.stop()


#  Build an abstract class Account with abstract methods deposit(), withdraw(), and get_balance().
# - Implement subclasses SavingsAccount and CurrentAccount.

from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass


class SavingsAccount(Account):
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        print(f"Savings Account Balance: {self.balance}")
        return self.balance


class CurrentAccount(Account):
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Current accounts may allow overdraft, but here we’ll keep it simple
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        print(f"Current Account Balance: {self.balance}")
        return self.balance


# Example usage
sv = SavingsAccount(1000)
sv.get_balance()
sv.deposit(500)
sv.withdraw(300)

cv = CurrentAccount(2000)
cv.get_balance()
cv.deposit(200)
cv.withdraw(2500)  # will fail due to insufficient funds

# - Create an abstract class Shape3D with abstract methods volume() and surface_area().
# - Implement subclasses Cube and Sphere.

from abc import ABC , abstractmethod
import math
class Shape3D(ABC):
    @abstractmethod
    def volume(self):
        pass
    @abstractmethod
    def surface_area(self):
        pass

class Cube(Shape3D):
    def __init__(self, side):
        self.side = side
    def volume(self):
        print(f"volume of the cube: {self.side**3}")
    def surface_area(self):
        print(f"Surface of the cube: {6*self.side**2}")
class Sphere(Shape3D):
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        print(f"Volume of Sphere: {(4/3) * math.pi * (self.radius ** 3)}")

    def surface_area(self):
        print(f"Surface Area of Sphere: {4 * math.pi * (self.radius ** 2)}")

c = Cube(4)
c.volume()
c.surface_area()

s = Sphere(3)
s.volume()
s.surface_area()