# 1. What is vectorization? 
Vectorization means applying operations to entire arrays at once instead of looping through elements one by one.

### Without NumPy (slow) 
nums = [1, 2, 3] 
result = [] 
for x in nums: 
    result.append(x * 2) 

### With NumPy (fast) 
arr = np.array([1, 2, 3]) 
print(arr * 2) 

---
# 2. Difference between list and NumPy operations 

| Feature    | Python List               | NumPy Array                                 |
| ---------- | ------------------------- | ------------------------------------------- |
| Speed      | Slow                      | Fast                                        |
| Operations | Manual loops              | Vectorized                                  |
| Memory     | Inefficient               | Compact                                     |
| Data type  | Mixed                     | Homogeneous                                 |
| Example    | `[1,2]+[3,4] = [1,2,3,4]` | `np.array([1,2]) + np.array([3,4]) = [4,6]` |

# 3. What are aggregation functions? 
- Functions that summarize data into a single value.
- Examples:
    - sum()
    - mean()
    - max()
    - min()
# 4. What is axis? 
Refers to the dimension along which an operation is performed.
    - axis=0 → column-wise (down rows).
    - axis=1 → row-wise (across columns).
### Example
arr = np.array([[1, 2], [3, 4]]) 
print(np.sum(arr, axis=0))  # Column-wise 
print(np.sum(arr, axis=1))  # Row-wise 
# 5. Why NumPy is faster? 
    - Written in C (low-level optimization)
    - Uses contiguous memory
    - Supports vectorization