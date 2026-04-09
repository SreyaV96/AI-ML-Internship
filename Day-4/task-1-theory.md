# Task 1: Theory 
## 1. Explain file handling with examples 
File handling allows to create, read, write, and manipulate files stored on disk
- The key function for working with files in Python is the open() function.
- Four different methods for opening a file:
  - r - Read - Read existing file 
  - w - Write - Create/overwrite file 
  - a - Append - Add data without deleting
  - x - Create - create new file only 
-  we can specify if the file should be handled as binary or text mode.
  - "t" - Text - Default value. Text mode
  - "b" - Binary - Binary mode (e.g. images)
```python
open("file.txt", "rt")  # Text mode
open("image.jpg", "rb") # Binary mode
```
### Reading from a File 
```python
file = open("demo.txt", "r") 
content = file.read() 
print(content) 
file.close() 
```
Using the **with** statement
```python
  with open("demo.txt") as f:
  print(f.read())
```
#### Read Line by Line 
Useful for large files
```python
file = open("demo.txt", "r") 
for line in file: 
    print(line) 
file.close() 
```
```python
with open("demo.txt") as f:
  print(f.readline())
```
### Writing to a File 
- "a" - Append - will append to the end of the file
- "w" - Write - will overwrite any existing content
```python 
with open("demo.txt", "a") as f:
  f.write("Now the file has more content!")
```
```python
with open("demo.txt", "w") as f:
  f.write("Oops! Previous content deleted.")
```
### Create a New File
``` python
f = open("myfile.txt", "x")
```
### Delete File
- import the OS module, and run its os.remove() function
```python 
import os
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else:
    print("File does not exist")
```
- delete folder
```python
import os
os.rmdir("myfolder")
```
---
## 2. Difference between read, write, append 

### 1. Read (`r`)
- Opens file for reading only  
- File **must exist**, otherwise raises an error  
- Does **not modify** the file  
```python
with open("demo.txt", "r") as f:
    content = f.read()
    print(content)
```
### 2. Write (w)
- Opens file for writing
- Creates file if it doesn’t exist
- Deletes all existing content before writing
``` python
with open("demo.txt", "w") as f:
    f.write("New content")
```
### 3. Append (a)
- Opens file for adding content
- Creates file if it doesn’t exist
- Adds data to the end of the file
```python
with open("demo.txt", "a") as f:
    f.write("\nAdded content")
```
## 3. What is exception handling? 
- An exception is an error that occurs during program execution. Eg:Division by zero, File not found, invalid input etc.
- Exception Handling is a process used to manage runtime errors so that the program doesn't crash.
- Python uses the following keywords to handle exceptions:
  - **try**
  - **except**
  - **else**
  - **finally**
### 1. Basic Try-Except 
```python
try: 
    x = int(input("Enter number: ")) 
    print(10 / x) 
except: 
    print("Something went wrong") 
```
### 2. Specific Exceptions 
Always prefer specific exceptions 
``` python
try: 
    x = int(input("Enter number: ")) 
    print(10 / x) 
except ZeroDivisionError: 
    print("Cannot divide by zero") 
except ValueError: 
    print("Please enter valid number") 
```
### 3.Else Block 
```python
try: 
    x = int(input()) 
except: 
    print("Error") 
else: 
    print("No error occurred") 
  Runs only if no error occurs 
```
### 4.Finally Block 
```python
try: 
    print("Running") 
except: 
    print("Error") 
finally: 
    print("This always runs") 
```
  Used for: 
• Closing files 
• Cleaning resources 
## 4. Why use try-except? 
- Prevents sudden program termination  
- Handles unexpected errors gracefully  
- Improves user experience  
- Allows debugging and error tracking  
- Maintains normal program flow  
```python
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except:
    print("Index out of range")
```
## 5. Explain finally block with example 
- It is used to execute code that **always runs**, regardless of whether an exception occurs or not.
- Executes after `try` and `except` blocks 
- Commonly used for cleanup operations (closing files, releasing resources)
```python
try:
    file = open("demo.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()
```