# 1. What is a Decision Tree? 
- A Decision Tree is a supervised machine learning algorithm used for classification and regression tasks. 
- It represents decisions and their possible outcomes in a tree-like structure. 
- The model learns a series of rules from the data to make predictions.
### Example: Weather and Playing Cricket

```text
Is Weather Sunny?
        |
    Yes / \ No
       /   \
Play     Don't Play
```

The tree uses conditions to determine the final outcome.


### Core Structure of a Decision Tree
- Root Node: The topmost node representing the entire initial dataset.
- Internal / Decision Nodes: Evaluation points testing a specific feature value.
- Branches / Edges: Conjunctions representing outcomes of a rule or test.
- Leaf / Terminal Nodes: The bottom endpoints that hold the final class label.

# 2. What is a Root Node? 
The **Root Node** is the first and top-most node of a Decision Tree. It represents the feature that best splits the data.

### Example

```text
Is Weather Sunny?
```

Here, **Weather** is the root node because it is the first decision made by the tree.

# 3. What is a Branch? 
A **Branch** is a path that connects nodes and represents the outcome of a condition.

### Example

```text
Is Weather Sunny?
      /      \
    Yes       No
```

The **Yes** and **No** paths are branches.


# 4. What is a Leaf Node? 
A **Leaf Node** is the final node in a Decision Tree where a prediction or decision is made.

### Example

```text
Is Weather Sunny?
      /      \
    Yes       No
     |         |
   Play    Don't Play
```

Here:

- **Play** is a leaf node.
- **Don't Play** is a leaf node.

No further decisions are made after reaching a leaf node.

# 5. Advantages of Decision Trees? 
1. Easy to understand and interpret.
2. Easy to visualize.
3. Works with both numerical and categorical data.
4. No need for feature scaling.
5. Can handle non-linear relationships.
6. Helps identify the most important features.
7. Provides clear decision rules.