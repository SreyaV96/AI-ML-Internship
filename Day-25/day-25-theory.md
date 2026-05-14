# 1. Why NumPy is important? 
NumPy is the backbone of numerical computing in Python.
- It provides fast array operations compared to native Python lists.
- Enables linear algebra, Fourier transforms, and advanced math efficiently.
- Forms the foundation for libraries like Pandas, SciPy, TensorFlow, and PyTorch.
- Its optimized C-based implementation makes it crucial for large-scale data processing.

---

# 2. What is vectorization? 
Vectorization means replacing explicit loops with array-based operations.
- Instead of iterating element by element, operations are applied to the entire array at once.
- This improves speed, readability, and efficiency.
- Example:
    ```python
    import numpy as np
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    result = a + b  # vectorized addition
    ```

---

# 3. Why shape matters in ML? 
Shape defines dimensions of data (rows, columns, channels).
- Why critical:
    - Models expect specific input shapes
    - Mismatched shapes → runtime errors
    - Wrong shape can affect training and predictions.
    - Determines how data flows through layers (especially in neural networks)
    - Shape consistency ensures proper matrix multiplications and transformations in neural networks.
---

# 4. What is normalization? 
Normalization scales data to a standard range (usually 0–1).
- Improves model performance.
- Prevents features with large values from dominating learning.
- Speeds up training.
- Common methods:
    - Min-Max scaling → values between 0 and 1.
        - Formula:
            - X_norm = (X - X.min()) / (X.max() - X.min())
    - Z-score standardization → mean = 0, variance = 1.

---

# 5. What is feature extraction? 
- Feature extraction transforms raw data into meaningful inputs for ML.
- Reduces dimensionality while preserving important information.
- Helps models focus on relevant patterns instead of noise.
### Examples:
 - text → TF-IDF, word embeddings.
 - images → edges, textures, CNN features.
 - audio → MFCCs (Mel-frequency cepstral coefficients).
 
---

