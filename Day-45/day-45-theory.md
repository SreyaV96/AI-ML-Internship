# 1. What is YOLOv8? 
YOLOv8 (You Only Look Once version 8) is a state-of-the-art real-time object detection model developed by Ultralytics. It can detect, classify, and track objects in images and videos with high speed and accuracy. YOLOv8 is the latest major version in the YOLO family and supports tasks such as object detection, segmentation, classification, and pose estimation.
# 2. What is a pretrained model? 
- A pretrained model is a machine learning model that has already been trained on a large dataset before being used for a specific task. 
- Instead of training from scratch, users can load the pretrained weights and use them directly or fine-tune them on their own dataset. 
-Example: yolov8n.pt is a pretrained YOLOv8 model trained on the COCO dataset.
# 3. What is a confidence score? 
A confidence score is the probability assigned by the model indicating how certain it is that a detected object belongs to a particular class.or it is the Confidence level of prediction. 
- Example:
    - Person → 0.97 (97%)
    - Dog → 0.94 (94%)
    - Car → 0.90 (90%)
- Higher confidence scores indicate greater certainty in the prediction.
# 4. Why is YOLOv8 popular? 
- Fast real-time object detection
- High detection accuracy
- Easy to use with Python
- Supports multiple computer vision tasks
- Pretrained models are readily available
- Works efficiently on both CPU and GPU
- Well-documented and actively maintained by Ultralytics
# 5. Difference between YOLOv8n and YOLOv8x?
| Feature         | YOLOv8n               | YOLOv8x               |
| --------------- | --------------------- | --------------------- |
| Size            | Nano (smallest)       | Extra Large           |
| Speed           | Very Fast             | Slower                |
| Accuracy        | Lower                 | Higher                |
| Memory Usage    | Low                   | High                  |
| Suitable For    | Edge devices, laptops | High-performance GPUs |
| Model File Size | Small                 | Large                 |
