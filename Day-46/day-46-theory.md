# 1. What is a class? 
- A class is the category or label assigned to an object by the detection model.
- Examples:
    - Person
    - Car
    - Dog
    - Bicycle
    - Chair

If the model detects a dog, its class is "dog".
# 2. What is a bounding box? 
A bounding box is a rectangular box drawn around a detected object to indicate its location in an image.
- It helps indicate:
    - Object position
    - Object size
    - Object category

- Example:

```text
+----------------+
|      DOG       |
|                |
+----------------+
```

#### Bounding Box Information

- X-coordinate
- Y-coordinate
- Width
- Height
- Confidence Score 
  

# 3. What is confidence score? 
A confidence score indicates how certain the model is that the detected object belongs to a particular class.
# 4. What is confidence threshold? 
A confidence threshold is the minimum confidence score required for a detection to be displayed.
- Example:

```python
conf = 0.5
```

Only detections with confidence ≥ 0.5 will be shown.
# 5. Why are bounding boxes important? 
Bounding boxes help us:
- Locate objects in an image
- Count objects
- Track objects in videos
- Measure object size and position