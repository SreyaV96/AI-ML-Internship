# 1. What is Logistic Regression? 
- Logistic Regression is a supervised machine learning algorithm used for classification problems. It predicts the probability that an input belongs to a particular class and then assigns a class label based on that probability.
- example:
    - Pass or Fail
    - Spam or Not Spam
    - Disease or No Disease

# 2. Why is it used? 
- Classification tasks: Predicting whether an email is spam or not, whether a patient has a disease, etc.
- Probability estimation: It provides probabilities, making it useful for decision-making.
- Binary and multiclass problems: It handles binary classification directly and can be extended to multinomial classification. 

# 3. What is Binary Classification?
- Binary Classification is a classification problem where there are only two possible classes. 
- Logistic Regression is most commonly used for binary classification.
- Examples: Pass/Fail, Spam/Not Spam, Fraud/Not Fraud.

# 4. What is a Class Label? 
- A Class Label is the category or outcome that the model predicts.
- The class label is usually stored in the target variable (y)
# 5. Difference between Linear and Logistic Regression? 

| Feature                 | Linear Regression                    | Logistic Regression                                    |
| ----------------------- | ------------------------------------ | ------------------------------------------------------ |
| **Purpose**             | Predicts continuous numerical values | Predicts categorical classes                           |
| **Type of Problem**     | Regression                           | Classification                                         |
| **Output**              | Any real number                      | Probability between 0 and 1, then converted to a class |
| **Target Variable**     | Continuous                           | Categorical                                            |
| **Examples**            | House Price, Salary, Temperature     | Pass/Fail, Spam/Not Spam, Disease/No Disease           |
| **Output Range**        | (-∞, +∞)                             | 0 to 1                                                 |
| **Prediction Function** | Linear Equation                      | Sigmoid Function                                       |
| **Formula**             | y = b₀ + b₁x₁ + b₂x₂ + ...           | p = 1 / (1 + e⁻ᶻ)                                      |
| **Evaluation Metrics**  | MSE, RMSE, MAE, R² Score             | Accuracy, Precision, Recall, F1-Score                  |
| **Graph Shape**         | Straight line                        | S-shaped (Sigmoid Curve)                               |
| **Goal**                | Estimate a quantity                  | Determine a class                                      |
