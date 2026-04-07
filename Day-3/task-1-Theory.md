# 1. What is a list? 
List is a built-in data structure used to store an ordered collection of items
- Allows duplicate elements
- **Mutable**: list elements can be changed, updated, added, or removed after the list is created.
- **Ordered**: elements maintain the order in which they are inserted.
- **Index-based**: elements are accessed using their position, starting from index 0.
- **Heterogeneous**: a list can store different data types such as integers, strings, booleans and even other lists.
- Square brackets [] are used to create a list directly.
- Also created using list() constructor.
- eg : a = [1, "hello", 3.5, True]
## Common list operations
### 1. Add Elements
- append(): Add an element at the end . eg: a.append(10) 
- extend(): Add multiple elements to the end .eg: a.extend([5,10,15])
- insert(): Add an element at a specific position. eg: a.insert(5,"Ann")
### 2. Remove elements
- remove(): Removes the first occurrence of an element. eg: a.remove("Hello")
- pop(): Removes the element at a specific index or the last element if no index is specified. eg:a.pop()
- del(): Deletes an element at a specified index.eg. del a[2]
- clear(): removes all items.
### 3. Updating Elements 
- Elements can be updated by assigning new values using their index.
- eg:
``` python
a = [1, 3.5, 10, 'Ann', 'hello ', '29']
a [0]=23
print(a)
```
### 4. Searching & Checking
Ways to inspect what is inside your list.

- len(): Returns the total number of items.

- in operator: Checks if an item exists in the list ("apple" in fruits).

- index(): Returns the index of the first occurrence of a value.

- count(): Returns how many times a value appears in the list.

### 5. Ordering and Sorting
These operations help organize your data.

- sort(): Sorts the list in place (ascending by default). Use sort(reverse=True) for descending.

- reverse(): Reverses the order of the items in the list in place.

- sorted(): A built-in function that returns a new sorted list without changing the original one.

### 6. Built-in Mathematical Operations 

- max(): Finds the largest value.

- min(): Finds the smallest value.

- sum(): Calculates the total of all elements.

### 7. Slicing (The : Operator)
- Slicing allows you to retrieve a specific portion of a list.

- Syntax: list[start:stop:step]
```python
num = [0, 1, 2, 3, 4, 5]

print(num[1:4])  #o/p [1, 2, 3] (index 1 to 3)
```
### 8. List Concatenation & Repetition
```python
a = [1, 2]
b = [3, 4]

print(a + b)   #o/p [1, 2, 3, 4]
print(a * 2)   #o/p [1, 2, 1, 2]
```
### 8 Looping Through Lists
```python
nums = [1,2,3]
for x in nums:
    print(x)
```
---
# 2. Difference Between List and Tuple
Lists and tuples are both used to store collections of items. However, they differ in mutability, performance, and typical use cases.

### Comparison

| Feature        | List                          | Tuple                         |
|----------------|-------------------------------|-------------------------------|
| Syntax         | `[ ]`                         | `( )`                         |
| Mutability     | Mutable                       | Immutable                     |
| Performance    | Slightly slower               | Slightly faster               |
| Methods        | several built in methods      | Fewer built in methods        |
| Use Case       | Dynamic data                  | Fixed/constant data           |

---

# 3. What is a dictionary? 
A dictionary is a built-in data structure that stores data in key-value pairs
- **ordered** : As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
- Stores data in **key : value** format  
- **Mutable**: dictionary elements can be changed, updated, added, or removed after creation  
- **Keys are unique**: duplicate keys are not allowed  
- **Key-based access**: values are accessed using keys instead of indexes  
- **Heterogeneous**: can store different data types (integer, string, list, etc.)  
- Curly braces {} are used to create a dictionary directly  
- Also created using dict() constructor  
- eg : student = {"name": "Ann Marry", "age": 21, "grade": "A"}
## Dictionary operations
### 1. Add Elements
- New key–value pairs can be added using assignment  
  - eg : student["city"] = "London"

### 2. Update Elements
- Existing values can be updated using keys  
  - eg : student["age"] = 25
### 3. Add or Update Multiple Elements
- update(): Adds or updates multiple key–value pairs at once  
- - If the key exists → value is updated  
- If the key does not exist → new key–value pair is added  
  - eg : student.update({"city": "London", "age": 25})

### 3. Remove Elements
- pop(): Removes element using key  
  - eg : student.pop("grade")

- del(): Deletes element using key  
  - eg : del student["age"]

- clear(): Removes all elements  
  - eg : student.clear()
### 4. Access Elements
- Values are accessed using keys  
  - eg : student["name"]

- get(): Safe access (returns None if key not found)  
  - eg : student.get("name")

### 5. Searching & Checking
- in operator: Checks if key exists  
  - eg : "name" in student

- len(): Returns number of key–value pairs  

### 6. Retrieving Keys and Values
- keys(): Returns all keys  
  - eg : student.keys()

- values(): Returns all values  
  - eg : student.values()

- items(): Returns key–value pairs  
  - eg : student.items()

### 7. Looping Through Dictionary
```python
student = {"name": "Ann", "age": 23}

for key, value in student.items():
    print(key, value)
```
---
# 4. What is a set? 
A Set is a built-in data structure used to store an unordered collection of unique elements.
- **Unordered**: elements do not maintain insertion order.  
- **Mutable**: elements can be added or removed (but individual elements must be immutable) . 
- **No duplicates**: automatically removes duplicate values.
- **Not index-based**: elements cannot be accessed using index.  
- **Heterogeneous**: can store different data types (int, string, tuple, etc.).  
- Curly braces `{}` are used to create a set. 
- Also created using `set()` constructor 

## Set Operations
### 1. Add Elements
- **add()**: Adds a single element  
  - eg : s.add(10)

- **update()**: Adds multiple elements  
  - eg : s.update([20, 30])

### 2. Remove Elements
- **remove()**: Removes element (error if not found)  
  - eg : s.remove(10)

- **discard()**: Removes element (no error if not found)  
  - eg : s.discard(20)

- **pop()**: Removes a random element  
  - eg : s.pop()

- **clear()**: Removes all elements  
  - eg : s.clear()

### 3. Mathematical Operations

- **union() ( | )**: Combines elements from both sets  
  - eg : a | b

- **intersection() ( & )**: Common elements  
  - eg : a & b

- **difference() ( - )**: Elements in first set but not in second  
  - eg : a - b

- **symmetric_difference() ( ^ )**: Elements in either set but not both  
  - eg : a ^ b

### 4. Comparison
- **issubset()**: Checks if set is subset  
  - eg : a.issubset(b)

- **issuperset()**: Checks if set is superset  
  - eg : a.issuperset(b)

- **isdisjoint()**: Checks if no common elements  
  - eg : a.isdisjoint(b)

### 5. Looping Through Set
```python
s = {1, 2, 3}

for x in s:
    print(x)
```
---
# 5. What is list comprehension? 
List comprehension is a concise way to create lists using a single line of code.
- Provides a short and readable syntax for creating lists  
- Replaces traditional loops for list creation  
- Can include conditions for filtering elements  (if)
- Improves code readability and performance 
- Syntax: new_list = [expression for item in iterable if condition]
``` python
nums = [1, 2, 3, 4, 5, 6]

even = [x for x in nums if x % 2 == 0]
print(even)   # o/p [2, 4, 6]