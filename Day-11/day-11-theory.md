# 1. What is inheritance? 
Inheritance allows a class to reuse properties and methods from another class.
- Parent Class → Base class 
- Child Class → Derived class 
### Example
```python
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    pass

d = Dog()
d.sound()
```
---
# 2. What is method overriding? 
- Method overriding happens when a child class provides its own version of a method already defined in the parent class.
- Child class can modify parent class method. 
### Example
```python
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()
```
---
# 3. What is encapsulation? 
Encapsulation means hiding internal data and controlling access. 
### Example
```python
class Student: 
    def __init__(self, name, marks): 
        self.name = name 
        self.__marks = marks   # private variable 
    def get_marks(self): 
        return self.__marks 
s = Student("Sara", 90) 
print(s.get_marks()) 
```
---
# 4. What is private variable? 
- A private variable is a variable that should not be accessed directly outside the class.
- In Python, private variables are written with double underscore __.
---
# 5. Why OOP is used in real projects? 
OOP is used because it makes programs easier to build and manage.
- Reusability – Through inheritance, existing code can be reused in new classes, reducing duplication.
- Security – Encapsulation hides internal data and exposes only necessary parts.
- Modularity – Large programs are divided into small independent objects for easier development and testing.
- Flexibility – Polymorphism allows one interface to work with different object types.
- Maintainability – Organized code is easier to update and debug.
- Scalability – Suitable for building large applications.
