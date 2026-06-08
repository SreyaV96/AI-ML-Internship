# 1. What is Random Forest? 
Random Forest is a supervised machine learning algorithm that combines multiple Decision Trees to make more accurate and reliable predictions. It works by creating many trees and combining their outputs to produce the final result.

# 2. What is an Ensemble Method? 
An Ensemble Method is a technique that combines multiple machine learning models to improve prediction accuracy and reduce errors. Instead of relying on a single model, it uses the collective intelligence of several models.

# 3. What is Voting? 
Voting is the process used by Random Forest to make a final prediction. Each Decision Tree makes its own prediction, and the class that receives the majority of votes becomes the final output.
- Example:

| Tree | Prediction |
|--------|-----------|
| Tree 1 | Pass |
| Tree 2 | Pass |
| Tree 3 | Fail |
| Tree 4 | Pass |
| Tree 5 | Fail |

- Final Prediction: Pass (Majority Vote)

# 4. Advantages of Random Forest? 
- High prediction accuracy
- Reduces overfitting compared to a single Decision Tree
- Handles large datasets effectively
- Works well with both classification and regression problems
- Can handle missing values and noisy data
- Provides feature importance information

# 5. Difference between Decision Tree and Random Forest? 

| Decision Tree | Random Forest |
|--------------|--------------|
| Uses a single tree | Uses multiple trees |
| More prone to overfitting | Less prone to overfitting |
| Faster to train | Slower to train |
| Easy to interpret | More difficult to interpret |
| Lower prediction accuracy | Higher prediction accuracy |
| Sensitive to data changes | More stable and robust |