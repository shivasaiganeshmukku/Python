# 🔹 Advanced Challenges
# - Build a University Management System:
# - Base class: Person
# - Subclasses: Student, Professor, Staff
# - Add multilevel inheritance for GraduateStudent and PhDStudent.

class Person:
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)

    def display(self):
        print(f"Name: {self.name}")


class Student(Person):
    def __init__(self, stu_id, **kwargs):
        self.stu_id = stu_id
        super().__init__(**kwargs)

    def display(self):
        super().display()
        print(f"Student ID: {self.stu_id}")


class Professor(Person):
    def __init__(self, prof_id, **kwargs):
        self.prof_id = prof_id
        super().__init__(**kwargs)

    def display(self):
        super().display()
        print(f"Professor ID: {self.prof_id}")


class Staff(Person):
    def __init__(self, staff_id, **kwargs):
        self.staff_id = staff_id
        super().__init__(**kwargs)

    def display(self):
        super().display()
        print(f"Staff ID: {self.staff_id}")


class GraduateStudent(Student):
    def __init__(self, grad_id, **kwargs):
        self.grad_id = grad_id
        super().__init__(**kwargs)

    def display(self):
        super().display()
        print(f"Graduate Student ID: {self.grad_id}")


class PhDStudent(GraduateStudent):
    def __init__(self, phd_id, **kwargs):
        self.phd_id = phd_id
        super().__init__(**kwargs)

    def display(self):
        super().display()
        print(f"PhD Student ID: {self.phd_id}")


p = PhDStudent(name="Shiva", stu_id=6677, grad_id=111, phd_id=999)
p.display()
p = Professor(name="Dr. Smith", prof_id=123)
p.display()
p = Staff(name="John", staff_id=456)
p.display()

#Implement a Game Character System:
# - Base class: Character
# - Subclasses: Warrior, Mage, Archer
# - Add hybrid inheritance for a BattleMage (inherits from both Warrior and Mage).
class Character:
    def __init__(self,name, health):
        self.name = name
        self.health = health

    def display(self):
        print(f"Character: {self.name}, Health: {self.health}")

class Warrior(Character):
    def __init__(self,name, health, strength ):
        super().__init__(self,name, health)
        self.strength = strength
        

    def attack(self):
        print(f"{self.name} attacks with strength {self.strength}")
class Mage(Character):
    def __init__(self, name, health,mana):
        super().__init__(name, health)
        self.mana = mana

    def cast_spell(self):
        print(f"{self.name} casts a spell with mana {self.mana}")

class Archer(Character):
    def __init__(self, name, health, arrows):
        super().__init__(name, health)
        self.arrows = arrows

    def shoot(self):
        print(f"{self.name} shoots an arrow. Arrows left: {self.arrows} ")
class BattleMage(Warrior, Mage):
    def __init__(self,name,health,strength, mana):
        Warrior.__init__(self,name, health, strength)
        Mage.__init__(self,name, health, mana)

    def special_attack(self):
        print(f"{self.name} performs a Powerfull battle magic attack.! ")

bm = BattleMage("Shiva", 100, 90, 50)
bm.display()
bm.attack()
bm.cast_spell()
bm.special_attack()

# Demonstrate polymorphism with inheritance:
# - Create a base class Shape with method area().
# - Subclasses: Circle, Rectangle, Triangle.
# - Call area() on different objects using the same reference.'''
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(f"Area of Circle: {3.14 *self.radius **2}")
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width =width
        self.height= height
    def area(self):
        print(f"Area of Rectangle: {self.width * self.height}")

class Triangle(Shape):
    def __init__(self , width, height):
        
        self.width = width
        self.height = height
    def area (self):
        print(f"Area of Triangle: {0.5 * self.width * self.height}")
    
shapes = [Circle(5),Rectangle(4,6),Triangle(4,5)]
for shape in shapes:
    shape.area()