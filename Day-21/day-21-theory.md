# 1. What is reshape? 
Reshape means changing the structure (shape) of an array without changing its 
data. 
### Example: 
 - 1D → 2D 
 - 2D → 3D 

---

# 2. Rule of reshape 
Total number of elements must remain the same.
### Formula: 
Total elements before = Total elements after 
### Example:
- If an Array has 12 elements them 
    - Possible reshapes:
        - (3,4)
        - (2,6)
        - (2,2,3)

---

# 3. Difference between flatten and ravel 
| Feature                  | `flatten()`                              | `ravel()`                             |
| ------------------------ | ---------------------------------------- | ------------------------------------- |
| Copy or View             | Returns a **copy**                       | Returns a **view** (mostly)           |
| Memory Usage             | Uses more memory                         | Uses less memory                      |
| Speed                    | Slower                                   | Faster                                |
| Effect on Original Array | Changes do not affect original array | Changes may affect original array |

--- 

# 4. What is transpose? 
- Transpose means converting rows into columns and columns into rows. 
- If a matrix is named \( A \), its transpose is written as \( A^T \).
### Example

Original matrix:

\[
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\]

Transpose:

\[
\begin{bmatrix}
1 & 3 \\
2 & 4
\end{bmatrix}
\]

---

# 5. What is stacking? 
- Stacking means combining multiple arrays into one. 
- Types: 
    - Vertical stacking (row-wise) 
    - Horizontal stacking (column-wise) 

---

 

  
 