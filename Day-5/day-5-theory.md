# Task 1: Theory 
## 1. What is string? 
- A string is a sequence of characters used to store text data. 
- **Immutable** (cannot change directly) 
- **Indexed** (can access using index) 
- **Ordered** (maintains sequence) 
### Common Operations
  - 1. Concatenation (joining strings)
    ```python
       first = "Hello"
       second = "World"
       print(first + " " + second)
    ```
  - 2. Indexing (access characters)
    ```python
    text = "Python"
    print(text[0])  # o/p: P
    ```
  - 3. Slicing (extract part of string)
    ``python
    text = "Python"
    print(text[0:3])  # o/p :Pyt
    ```
### Methods
  - Upper Case
    ```python
    a = "Hello, World!"
    print(a.upper())
    ```
  - Lower Case
    ```python
    a = "Hello, World!"
    print(a.lower())
    ```
  - Remove Whitespace
    ```python
    a = "Hello, World!"
    print(a.strip())
    ```
  - Replace String
    ```python
    a = "Hello, AI"
    print(a.replace("AI", "ML"))
    ```
  -  Split & Join
 
    ```python
    text = "AI ML Python" 
    words = text.split(" ") 
    print(words) 
    new_text = " ".join(words) 
    print(new_text)
    ``` 
## 2. What is slicing? 
Slicing is a technique used to extract a portion  of a sequence like a string, list, or tuple using index positions.
- syntax : sequence[start : end : step]
    - start → index where slicing begins (included)
    - end → index where slicing stops (excluded)
    - step → interval between elements (optional)
      ```python
      text = "Python" print(text[0:3]) # Pyt 
      print(text[2:6]) # thon 
      print(text[:4]) # Pyth 
      print(text[::2]) # Pto
      ```
    - Negative Slicing 
    ```python
     text = "Python" 
     print(text[-1]) # n 
     print(text[-4:-1]) # hon
## 3. What is nested data structure? 
A nested data structure is a data structure that contains another data structure inside it. ie,data stored within data.
### Why Nested Data
 - Shows real-world relationships
 - Keeps related data together
 - Used in APIs and JSON data
 - Helps store complex data
### Examples of Nested Data Structures in Python
#### 1. Nested List
- A list inside another list
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
#### 2. Nested Dictionary
- Dictionary inside a dictionary
```python
    student = {
    "name": "Arjun",
    "marks": {
        "math": 90,
        "science": 85
    }
   }
```

#### 3. List of Dictionaries
- List containing dictionaries
 ```python
    students = [
    {"name": "A", "age": 20},
    {"name": "B", "age": 22}
     ]
```
#### 4. Dictionary with List
- Dictionary containing a list
```python
data = {
    "fruits": ["apple", "banana", "mango"]
}
```
#### 5. Mixed Nested Structure
- Dictionary → List → Dictionary
```python
school = {
    "class1": [
        {"name": "A", "marks": 80},
        {"name": "B", "marks": 85}
    ]
}
```
## 5. Why modules are important? 
1. **Code Reusability**  
   Write code once and reuse it in different programs  

2. **Better Organization**  
   Splits large programs into smaller, manageable files  

3. **Easy Maintenance**  
   Easier to update and fix bugs in one place  

4. **Avoids Repetition**  
   Reduces duplicate code  

5. **Improves Readability**  
   Makes code clean and easier to understand  

6. **Access to Built-in Functions**  
   Use existing modules like `math`, `random`, etc.  
