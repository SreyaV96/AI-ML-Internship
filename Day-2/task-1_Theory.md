# Why Python is used in AI?

Python is one of the most widely used programming languages in Artificial Intelligence (AI) and Machine Learning (ML). Its simplicity, powerful libraries, and strong community support make it a preferred choice for developers and researchers.
## Key Reasons
### 1. Extensive Libraries and Frameworks
Python provides a rich ecosystem of libraries that simplify AI development:
- Machine Learning: Scikit-learn  
- Deep Learning: TensorFlow, PyTorch, Keras  
- Data Processing: NumPy, Pandas  
- Visualization: Matplotlib, Seaborn  
These libraries provide pre-built functions, reducing development time and simplifying complex implementations.

### 2. Simple and Readable Syntax
- Easy to learn and implement  
<<<<<<< HEAD
- simple syntax  
=======
- Simple syntax  
>>>>>>> d26f1d3 (Day 3 completed)
- Uses indentation instead of complex symbols  
This improves code readability, maintainability, and reduces errors.
### 3. No Compilation Required
- Python is an interpreted language  
- Code executes line by line without recompilation  
This enables rapid prototyping and iterative experimentation, which is essential in AI development.

### 4. Platform Independence
Python is compatible with multiple operating systems:
- Windows  
- macOS  
- Linux  
Code can be executed across platforms without modification.

### 5. Strong Community Support
- Large and active developer community  
- Extensive documentation and tutorials  
- Continuous open-source contributions  
This ensures easier learning, troubleshooting, and access to updated tools.

## Conclusion
Python is preferred for AI because it offers:
- Powerful libraries and frameworks  
- Simple and readable syntax  
- Faster development and testing  
- Cross-platform compatibility  
- Strong community support  
---

# What are variables?
- A variable acts as a container that stores a value, which can be accessed and modified later in the program.
- Eg:
   ```python
   x = 100
   name = "Hari"
  x stores an integer value
  name stores a string value
 - Variables do not need to be declared with any particular type, and can even change type after they have been set.
 - Variable names are case-sensitive. eg :a = 4, A = "Sally". This will create two variables
## Rules for Naming Variables
 - Must start with a letter or underscore _
 - Cannot start with a number
 - Cannot use reserved keywords (e.g., if, for, class)
 - Variable names are case-sensitive (age, Age and AGE are three different variables)
 - Should be meaningful and readable
   
---
# What is a data type?
data type is an attribute associated with a piece of data that tells a computer system how to interpret its value. or it is the type of value a variable can store.

## Built-in Data Types in Python
### 1. Numeric Types
- `int` → Integer values (e.g., 10, -5)  
- `float` → Decimal values (e.g., 3.14)  
- `complex` → Complex numbers (e.g., 2 + 3j)  
### 3. Sequence Types 
- `str` → String (text) (e.g., "Hello") 
- `list` → Ordered, mutable collection (e.g., [1, 2, 3])  
- `tuple` → Ordered, immutable collection (e.g., (1, 2, 3))  

### 3. Set Type
- `set` → Unordered collection of unique elements (e.g., {1, 2, 3})  
- `frozenset`→ immutable
### 4. Mapping Type
- `dict` → Key-value pairs (e.g., {"name": "Allen", "age": 20})  

### 5. Boolean Type
- `bool` → True or False  

### 6. None Type
- `NoneType` → Represents no value (`None`)  

---

# Difference between if and loop

In Python, `if` and loops are used to control how a program runs, but they have different purposes.

## `if` Statement

- An `if` statement is used to check a condition.
- If the condition is true, the code runs  
- If the condition is false, the code is skipped  
- Executes only once  (unless nested or combined with loops)

  eg:
   ```python
    marks = 80

    if marks > 50:
      print("You passed")

## Loop (`for` / `while`)

- A loop is used to repeat a block of code multiple times.
- Used for repetition (iteration)
- Executes a block of code multiple times
- Runs until a condition becomes false or iteration ends  

  eg:
  ```python
     for i in range(3):
       print("Hello")
<<<<<<< HEAD
=======
    
>>>>>>> d26f1d3 (Day 3 completed)

---

# What is a Function?

- A function is a reusable block of code designed to perform a single, specific task.
- A function is defined using the `def` keyword  
- It helps avoid repeating the same code  
- Improves readability and structure of programs  

## Types of Functions

- **Built-in functions** → `print()`, `len()`, `type()`  
- **User-defined functions** → Created by the programmer  
  eg:
  ```python
    def subtract(a, b):
     return a - b

     result = subtract(10, 4)
     print(result)
