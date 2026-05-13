# 1. What is NumPy random module? 
- The NumPy random module is a part of the NumPy library used to generate random numbers and random datasets in Python.
- It provides functions for:

    - Random integers
    - Random decimal numbers
    - Random arrays and matrices
    - Random selections and shuffling

---

# 2. Why random data is important?
Random data is important because it helps in:
    - Testing programs
    - Simulating real-world datasets
    - Machine learning experiments
    - Statistical analysis
    - Game development
    - Scientific research 

---

# 3. What is seed? 
- A seed is a starting value used to generate random numbers.
- Seed ensures the same random output every time

---

# 4. Difference between randint and rand 
| Feature           | `randint()`                          | `rand()`                                |
| ----------------- | ------------------------------------ | --------------------------------------- |
| Purpose           | Generates random integers            | Generates random decimal (float) values |
| Data Type         | Integer (`int`)                      | Float (`float`)                         |
| Range             | User-defined range                   | Between 0 and 1                         |
| Syntax            | `np.random.randint(low, high, size)` | `np.random.rand(shape)`                 |
| Common Use        | Random IDs, marks, counts            | Probability, ML data, decimal datasets  |

---

# 5. What is dataset simulation? 
- Dataset simulation means creating artificial data using random values.
- It is used when real data is unavailable.

---