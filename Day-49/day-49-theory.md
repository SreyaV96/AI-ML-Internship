# 1. What is an Epoch? 
An epoch is one complete pass of the entire training dataset through the model.

For example:
- If the dataset contains 32 images, then during 1 epoch, the model sees all 32 images once.
- During 10 epochs, the model sees the same 32 images ten times and learns from them repeatedly.

1 Epoch = One complete pass through all training data

# 2. What is Loss?
Loss is a measure of how wrong the model's predictions are compared to the actual labels.
- High loss indicates poor predictions.
- Low loss indicates better predictions.

During training, the model tries to minimize loss by adjusting its weights.

In YOLOv8:
- **Box Loss** measures bounding box localization accuracy.
- **Classification Loss** measures class prediction accuracy.
- **DFL (Distribution Focal Loss)** improves bounding box refinement.

# 3. What is Precision? 
*Precision** measures how many detected objects are actually correct.

**Formula:**

Precision = True Positives / (True Positives + False Positives)

**Example:**

- Model detects 10 helmets.
- 8 detections are correct.
- 2 detections are incorrect.

Precision = 8 / (8 + 2) = 0.8 (80%)

A high precision value means the model produces fewer false detections.

# 4. What is Recall? 
**Recall** measures how many actual objects the model successfully detects.

**Formula:**

Recall = True Positives / (True Positives + False Negatives)

**Example:**

- There are 10 helmets in the image.
- The model detects 8 of them.

Recall = 8 / (8 + 2) = 0.8 (80%)

A high recall value means the model misses fewer objects.

# 5. What is mAP? 
**mAP (Mean Average Precision)** is the primary evaluation metric used in object detection. It evaluates both classification accuracy and bounding box localization quality.

It is calculated using the Precision-Recall curve.

Common YOLO metrics:

- **mAP@0.5**: Detection is considered correct when IoU ≥ 0.5.
- **mAP@0.5:0.95**: Average mAP calculated across IoU thresholds from 0.5 to 0.95.
