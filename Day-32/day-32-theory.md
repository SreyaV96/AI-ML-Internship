# 1. What is Seaborn? 
Seaborn is a Python data visualization library built on top of Matplotlib.It provides a high-level interface for drawing attractive and informative statistical graphics.

---
# 2. Difference between Matplotlib and Seaborn 

| Feature           | Matplotlib         | Seaborn                             |
| ----------------- | ------------------ | ----------------------------------- |
| Level             | Low-level          | High-level                          |
| Complexity        | More code required | Less code                           |
| Design            | Basic visuals      | Attractive & modern                 |
| Statistical plots | Limited            | Advanced (boxplot, violin, heatmap) |
| Default styles    | Plain              | Styled automatically                |

---

# 3. Why Seaborn is important? 
- Simplifies complex visualizations
- Built-in themes improve readability
- Integrates well with Pandas DataFrames
- Provides statistical insights (distribution, relationships, trends)

---
# 4. What is statistical visualization? 
It refers to visualizing data distributions, relationships, and statistical summaries (e.g., histograms, boxplots, scatter plots).

---

# 5. What is box plot? 
- A box plot (box-and-whisker plot) summarizes a dataset using five-number summary:
 - Minimum (smallest value excluding outliers)
 - Q1 (25th percentile)
 - Median (Q2, 50th percentile)
 - Q3 (75th percentile)
 - Maximum (largest value excluding outliers)
- Outliers are detected using:
    -  **IQR = Q3 − Q1**
    -  **Lower bound = Q1 − 1.5 × IQR**
    -  **Upper bound = Q3 + 1.5 × IQR**
    -  Any value outside this range = outlier

---