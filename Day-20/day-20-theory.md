# 1. What is indexing? 
Indexing is selecting a single element from an array using its position.


---
# 2. What is slicing? 
Slicing extracts a subset of array using a range of indices.


---
# 3. Difference between indexing and slicing 
| Aspect    | Indexing       | Slicing               |
| --------- | -------------- | --------------------- |
| Output    | Single element | Sub-array             |
| Syntax    | `arr[i]`       | `arr[start:end:step]` |
| Dimension | Reduced        | Preserved             |
| Example   | `arr[2] → 30`  | `arr[1:3] → [20, 30]` |

# 4. What is boolean indexing? 
Selecting elements using True/False conditions.
### Example
```python 
arr[arr > 25]
# o/p [30 40] 
```

---
# 5. Why indexing is important in ML? 
- **Access data quickly**  
  Retrieve specific features, labels, or samples efficiently.

- **Data preprocessing**  
  Clean data, remove outliers, and filter rows using conditions.

- **Train-test split**  
  Divide datasets into training and testing parts.

- **Batch processing**  
  Select mini-batches for efficient model training.

- **Feature selection**  
  Choose important columns (features) for better models.

- **Handle images/tensors**  
  Extract regions, channels, or elements in multi-dimensional data.

- **Enable fast computation**  
  Works with vectorized operations in tools like NumPy, TensorFlow, PyTorch.

---
