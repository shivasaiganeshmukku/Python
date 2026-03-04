'''
🔹 Single Inheritance
- Create a Person class with attributes name and age.
- Derive a Student class that adds roll_number and marks.
- Write methods to display student details.
- Implement a Vehicle base class and a Car subclass.
- Add methods to calculate mileage.

🔹 Multiple Inheritance
- Create a Teacher class and a Mentor class.
- Derive a Guide class that inherits from both.
- Demonstrate how method resolution order (MRO) works.
- Implement a Writer class and a Speaker class.
- Create an Author class that inherits from both and shows combined behavior.

🔹 Multilevel Inheritance
- Create a Grandparent class → Parent class → Child class.
- Each should have a method introduce().
- Demonstrate calling methods across levels.
- Implement a Shape base class → Polygon subclass → Triangle subclass.
- Add methods to calculate area.

🔹 Hierarchical Inheritance
- Create a Animal base class.
- Derive Dog, Cat, and Bird classes.
- Each should override a method sound().
- Implement a BankAccount base class.
- Derive SavingsAccount and CurrentAccount classes with different interest rules.

🔹 Hybrid Inheritance
- Create a Person base class.
- Derive Employee and Student classes.
- Create a WorkingStudent class that inherits from both.
- Demonstrate how Python resolves conflicts using MRO.
- Implement a Device base class.
- Derive Phone and Camera classes.
- Create a Smartphone class that inherits from both.

🔹 Advanced Challenges
- Build a University Management System:
- Base class: Person
- Subclasses: Student, Professor, Staff
- Add multilevel inheritance for GraduateStudent and PhDStudent.
- Implement a Game Character System:
- Base class: Character
- Subclasses: Warrior, Mage, Archer
- Add hybrid inheritance for a BattleMage (inherits from both Warrior and Mage).
- Demonstrate polymorphism with inheritance:
- Create a base class Shape with method area().
- Subclasses: Circle, Rectangle, Triangle.
- Call area() on different objects using the same reference.'''

# Single Inheritance
# Create a Person class with attributes name and age.
class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

p = Person("Shiva", 22)
p.display()

# Derive a Student class that adds roll_number and marks.
class Student:
    def __init__(self, roll_number , marks):
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        print(f"roll Number {self.roll_number} marks are {self.marks}")

# Write methods to display student details.
B = Student("22RA1A6677","97")
B.display()

#Implement a Vehicle base class and a Car subclass.
#Add methods to calculate mileage.
class Vehicle:
    def __init__(self , make , model):
        self.make = make
        self.model = model

    def display(self):
        print(f"Make: {self.make}, Model: {self.model}")
class Car(Vehicle):
    def __init__(self , make , model , mileage):
        super().__init__(make , model)
        self.mileage = mileage

    def display(self):
        super().display()
        print(f"Mileage: {self.mileage} km/l")
c = Car("Toyota" , "Camry" , 15)
c.display()

#🔹 Multiple Inheritance
# Create a Teacher class and a Mentor class.
class Teacher:
    def __init__(self,subject):
        self.subject = subject
    def teach(self):
        print(f"Teaching {self.subject}")
class Mentor:
    def __init__(self, experience):
        self.experience  = experience
    def guide(self):
        print(f"Guiding with {self.experience} years of experience")
# Derive a Guide class that inherits from both.
class Guide(Teacher , Mentor):
    def __init__(self, subject, experience):
        Teacher.__init__(self, subject)
        Mentor.__init__(self, experience)
# Demonstrate how (Method Resolution Order) (MRO) works.
g = Guide("Math ", 10)
g.teach()
g.guide()
print(Guide.mro())#shows the order Python searches for methods

# Implement a Writer class and a Speaker class.
# Create an Author class that inherits from both and shows combined behavior.
class Writer:
    def __init__(self, genre):
        self.genre = genre
    def write(self):
        print(f"Writing {self.genre} books")
class Speaker:
    def __init__(self, topic):
        self.topic = topic
    def speak(self):
        print(f"Speaking on {self.topic}")
class Author(Writer , Speaker):
    def __init__(self, genre, topic):
        Writer.__init__(self, genre)
        Speaker.__init__(self, topic)
a = Author("Fiction", "Motivation")
a.write()
a.speak()

#🔹 Multilevel Inheritance
# Create a Grandparent class → Parent class → Child class.
class Grandparent:
    def introduce(self):
        print("I am the grandparent.")
class Parent(Grandparent):
    def introduce(self):
        print("I am the parent.")
class Child(Parent):
    def introduce(self):
        print("I am the child.")
# Each should have a method introduce().
g = Grandparent()
p = Parent()
c = Child()
g.introduce()
p.introduce()
c.introduce()

# Implement a Shape base class → Polygon subclass → Triangle subclass.
# Add methods to calculate area.
class Shape:
    def area(self):
        pass
class Polygon(Shape):
    def __init__(self,sides):
        self.sides = sides
class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__(3) # Triangle has 3 sides
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
t = Triangle(10, 5)
print(f"Area of the triangle: {t.area()}")

# 🔹 Hierarchical Inheritance
# Create a Animal base class.
class Animal:
    def sound(self):
        pass
# Derive Dog, Cat, and Bird classes.
class Dog(Animal):
    def sound(self):
        super().sound()
        print("dog barks")
class Cat(Animal):
    def sound(self):
        super().sound()
        print("cat meows")
class Bird(Animal):
    def sound(self):
        super().sound()
        print("bird chirps")
# Each should override a method sound().
d= Dog()
c = Cat()
b = Bird()
d.sound()
c.sound()
b.sound()

# Implement a BankAccount base class.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def display_balance(self):
        print(f"Balance: ${self.balance}")
# Derive SavingsAccount and CurrentAccount classes with different interest rules.
class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return self.balance * 0.04 # 4% interest
class CurrentAccount(BankAccount):
    def calculate_interest(self):
        return self.balance * 0.02 # 2% interest
s = SavingsAccount(1000)
c = CurrentAccount(2000)
s.display_balance()
c.display_balance()
print(f"Savings Account Interest: ${s.calculate_interest()}")
print(f"Current Account Interest: ${c.calculate_interest()}")

#🔹 Hybrid Inheritance
# - Create a Person base class.
# - Derive Employee and Student classes.
# - Create a WorkingStudent class that inherits from both.

class Person:
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)

    def display(self):
        print(f"Name: {self.name}")


class Employee(Person):
    def __init__(self, employee_id, **kwargs):
        self.employee_id = employee_id
        super().__init__(**kwargs)

    def display(self):
        super().display()
        print(f"Employee ID: {self.employee_id}")


class Student(Person):
    def __init__(self, student_id, **kwargs):
        self.student_id = student_id
        super().__init__(**kwargs)

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}")


class WorkingStudent(Employee, Student):
    def __init__(self, name, employee_id, student_id):
        super().__init__(name=name, employee_id=employee_id, student_id=student_id)


ws = WorkingStudent("Alice", "E123", "S456")
ws.display()

print(WorkingStudent.mro())

# Implement a Device base class.
# - Derive Phone and Camera classes.
# - Create a Smartphone class that inherits from both.
class Device:
    def __init__(self, brand, **kwargs):
        self.brand = brand
        super().__init__(**kwargs)

    def display(self):
        print(f"Brand: {self.brand}")
        super().display()


class Phone(Device):
    def __init__(self, phone_number, **kwargs):
        self.phone_number = phone_number
        super().__init__(**kwargs)
        super().display()


class Camera:
    def __init__(self, resolution, **kwargs):
        self.resolution = resolution
        super().__init__(**kwargs)

    def display(self):
        print(f"Resolution: {self.resolution}Mp")


class Smartphone(Phone, Camera):
    def __init__(self, brand, phone_number, resolution):
        super().__init__(brand=brand, phone_number=phone_number, resolution=resolution)


s = Smartphone("Samsung", "123-456-7890", 48)
s.display()


