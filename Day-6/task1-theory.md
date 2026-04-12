# 1. Steps in problem solving 
Follow these steps: 
1. Understand the problem 
2. Break into smaller steps 
3. Write logic (pseudo code) 
4. Convert to Python code 
5. Test with inputs 
---
# 2. What is algorithm? 
A finite, step-by-step set of instructions designed to solve a specific problem.
### Properties
- **Finite** → Must end after a limited number of steps  
- **Clear & Unambiguous** → Each step should be precise  
- **Input & Output Defined**  
- **Efficient** → Should use optimal time and space 
- **Language Independent** 
#### Example:
Algorithm to add two numbers:
1. Start  
2. Input A and B  
3. Compute Sum = A + B  
4. Display Sum  
5. Stop  
---

# 3. What is menu-driven program? 
A program that provides users with a list of options (menu) and performs actions based on the user’s choice.
- Uses loops to repeatedly display the menu  
- Uses conditional statements (`if`, `elif`, `else`) to handle choices  
- Continues running until the user selects an exit option  
### Example:

```python
while True: 
    print("1. Add") 
    print("2. Exit") 

    choice = int(input("Enter choice: ")) 

    if choice == 1: 
        a = int(input()) 
        b = int(input()) 
        print("Sum:", a+b) 

    elif choice == 2: 
        break 
```
---
# 4. Why logic is important in AI? 
Logic is a core part of Artificial Intelligence because it helps machines think, reason, and make decisions in a structured way.
Logic helps AI to:
- Think clearly
- Make decisions
- Stay consistent
- Explain results
---
# 5. Difference between list and dictionary 

| Feature     | List                          | Dictionary                         |
|-------------|-------------------------------|-------------------------------------|
| Definition  | Ordered collection of items   | Collection of key-value pairs       |
| Syntax      | `[1, 2, 3]`                   | `{"a": 1, "b": 2}`                  |
| Access      | By index (`list[0]`)          | By key (`dict["a"]`)                |
| Order       | Ordered                       | Ordered (Python 3.7+)               |
| Mutable     | Yes                           | Yes                                 |
| Duplicate   | Allowed                       | Keys must be unique                 |
| Use Case    | Store sequence of items       | Store mapped data (key → value)     |