# 1. What is list comprehension? 
List comprehension is a short and efficient way to create lists in Python using a single line of code.
- syntax
```python
[expression for item in iterable if condition]
```
### Example
```python
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)
```
---
# 2. Difference between list and set 
| Feature | List | Set |
|---|---|---|
| Order | Ordered | Unordered |
| Duplicates | Allowed | Not allowed |
| Indexing | Yes | No |
| Mutable | Yes | Yes |
| Syntax | `[ ]` | `{ }` |

---

# 3. What is generator? 
- A generator is a special function that returns values one at a time using yield instead of return.
- It saves memory because values are generated only when needed.
- Used in large data processing 
### Example
```python
def count(n): 
    for i in range(n): 
        yield i 

for num in count(5): 
    print(num) 
```
---
# 4. What is zip function? 
The Python zip() function is a built-in utility that aggregates elements from two or more iterables (like lists, tuples, or strings) into a single iterator of tuples.
```python
names = ["Ram", "Sam", "Tom"]
marks = [90, 85, 88]

result = zip(names, marks)
print(list(result))
```
---
# 5. What is enumerate? 
The enumerate() function in Python is a built-in function that allows you to iterate over an iterable (such as a list, tuple, or string) while also keeping track of the index of each item in the iterable.
```python
names = ["AI", "ML"] 
for i, name in enumerate(names): 
    print(i, name) 
```
---