# 1. What is OOP? 
Object-Oriented Programming (OOP) is a way of writing code using objects and classes. 
Instead of writing everything in functions, we organize code into: 
- Classes 
- Objects 
## Advantages of OOP
-  Better structure 
-  Reusability 
-  Easy to manage large projects 
-  Used in real-world applications 
---
# 2. Difference between class and object 
A class is a blueprint or template that defines properties (attributes) and behaviors (methods), while an object is a physical, concrete instance created from that class.
### Example
```python
class Car:
    color = "Red"
mycar = Car()
Car = Class
mycar = Object
```
---
# 3. What is constructor? 
- A constructor is used to initialize object values. 
- In Python, constructor is __init__()
```python
class Car:
    def __init__(self, color):
        self.color = color

c1 = Car("Blue")
```
---
# 4. What is method? 
A method is a function defined inside a class. It describes what an object can do.
### Example
```python
class Student: 
    def __init__(self, name, marks): 
        self.name = name 
        self.marks = marks 

    def display(self): 
        print(self.name, self.marks) 

s1 = Student("Alex", 75) 
s1.display() 
```
---
# 5. Why OOP is used?
OOP is used because it makes programs easier to build and manage.
- Reusability – Through inheritance, existing code can be reused in new classes, reducing duplication.
- Security – Encapsulation hides internal data and exposes only necessary parts.
- Modularity – Large programs are divided into small independent objects for easier development and testing.
- Flexibility – Polymorphism allows one interface to work with different object types.
- Maintainability – Organized code is easier to update and debug.
- Scalability – Suitable for building large applications.
---
