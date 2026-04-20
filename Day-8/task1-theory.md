## 1. What is Function?
A function is a reusable block of code that performs a specific task. It helps organize code and avoids repetition.

```python
def greet():
    print("Hello")
```
---
# 2. Difference Between `print()` and `return`

| Feature | `print()` | `return` |
|--------|-----------|----------|
| Purpose | Displays output to the user | Sends data back from a function |
| Storage | Cannot be reused directly | Can be stored in a variable |
| Function Flow | Continues to next line after printing | Exits function immediately |
| Usage | Can be used anywhere | Used only inside a function |
| Output Type | Shows value on screen | Gives value to caller |
| Default Result | No returned value | If omitted, returns `None` |
| Best Use | Debugging / displaying messages | Getting results for further use |

## Example

```python
def add(a, b):
    return a + b

def show_add(a, b):
    print(a + b)
result = add(2, 3)

print(result)      # 5
show_add(2, 3)    # 5
```
---
## 3. What is recursion?
Recursion is when a function calls itself to solve a problem.
-  Must have a base case 
-  Used in complex problems 
-  Important in algorithms 
## Example: Factorial 
```python
def factorial(n): 
    if n == 1: 
        return 1 
    return n * factorial(n-1) 
print(factorial(5)) 
```
---
# 4. What is Lambda Function?
- A lambda function is a small anonymous function.
- It can take any number of arguments, but can only have one expression.
- Syntax- lambda arguments : expression
- Lambda functions are commonly used with built-in functions like map(), filter(), and sorted()
## Example
```python
square = lambda x: x * x
print(square(5))
```
- map() 
```python
nums = [1, 2, 3] 
result = list(map(lambda x: x*2, nums)) 
print(result) 
```
- filter() 
```python
nums = [1, 2, 3, 4] 
result = list(filter(lambda x: x % 2 == 0, nums)) 
print(result)
```
- sorted()
```python
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
```
---
# 5. What is map() and filter()?
- map() applies a function to all items in a list.
- filter() selects items based on a condition.
## Example
```python
nums = [1, 2, 3]
print(list(map(lambda x: x * 2, nums)))
print(list(filter(lambda x: x > 1, nums)))
```
