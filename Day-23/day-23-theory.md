# 1. What is broadcasting? 
- Broadcasting is a feature in NumPythat allows arrays of different shapes to perform arithmetic operations together without manually reshaping them. 
- NumPy automatically expands the smaller array to match the larger array shape when possible.
# 2. Why broadcasting is important? 
- Reduces the need for loops
- Makes code faster and shorter
- Saves memory
- Simplifies mathematical operations on arrays
# 3. What are broadcasting rules? 
Two arrays are compatible for broadcasting when:
    - Their dimensions are equal, OR
    - One of the dimensions is 1
# 4. What happens with incompatible shapes? 
If shapes do not follow broadcasting rules, NumPy raises an error.
# 5. Advantages of broadcasting 
Advantages include:
    - Faster computation
    - Less code
    - Efficient memory usage
    - Easy mathematical operations
    - Better performance than loops