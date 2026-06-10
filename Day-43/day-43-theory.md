# 1. What is SVM? 
Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification and regression problems. It finds the best boundary (hyperplane) that separates different classes of data with the maximum margin.
#### Example:
- Classify students as Pass/Fail
- Detect Spam/Not Spam emails
- sentiment analysis
# 2. What is a Decision Boundary? 
A Decision Boundary is a line (2D), curve, or hyperplane that separates different classes in the dataset.
#### Example:
```text
Pass ● ● ● | ○ ○ ○ Fail
           ↑
   Decision Boundary
```

The SVM algorithm tries to find the best possible boundary between classes.
# 3. What are Support Vectors? 
- Support Vectors are the data points closest to the decision boundary.
- These points are very important because they determine the position of the boundary.
# 4. What is Margin? 
- The Margin is the distance between the decision boundary and the nearest support vectors.
- SVM tries to maximize this margin.
# 5. Advantages of SVM? 
- Works well with small and medium datasets.
- Effective in high-dimensional data.
- Less chance of overfitting.
- Good classification accuracy.
- Can handle linear and non-linear data using kernels.