# 1. What is KNN? 
K-Nearest Neighbors (KNN) is a machine learning algorithm used for classification and regression. It predicts the class of a new data point by looking at the classes of its nearest neighbors.
# 2. What does K mean in KNN? 
- K represents the number of nearest neighbors considered when making a prediction.
- Example:
    - K = 3 → Consider the 3 closest data points.
    - K = 5 → Consider the 5 closest data points.
# 3. Is KNN supervised or unsupervised? 
KNN is a Supervised Learning algorithm because it learns from labeled training data.
# 4. What is a neighbor? 
A neighbor is a nearby data point used to make predictions. The closeness is usually measured using a distance metric such as Euclidean Distance or Manhattan Distance.
# 5. Advantages of KNN? 
- Simple to use: Easy to understand and implement.works well with small dataset
- No training step: No need to train as it just stores the data and uses it during prediction.
- Few parameters: Only needs to set the number of neighbors (k) and a distance method.
- Versatile: Works for both classification and regression problems.