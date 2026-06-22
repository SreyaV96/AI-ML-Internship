# 1. What is Custom Object Detection? 
Custom Object Detection is the process of training an object detection model to recognize and locate objects specific to your own use case instead of using only pre-trained classes.
A custom dataset containing images and labels is used to train the model.
### Examples:
    - Helmet Detection
    - Vehicle Number plate Detection
    - Defect Detection in manufacturing
    - Product Detection 
# 2. What is Annotation? 
- Annotation is the process of labeling objects in images by drawing bounding boxes around them and assigning class names.
- In object detection, annotation involves:
    - Drawing a bounding box around an object.
    - Assigning a class label to that object.
# 3. What is data.yaml? 
- data.yaml is a configuration file used by YOLO to describe the dataset.
- It tells the model:
    - Where training images are stored
    - Where validation images are stored
    - Number of classes
    - class names
### Example
train: dataset/images/train
val: dataset/images/val

nc: 1

names:
  0: Helmet
# 4. What is an Epoch?
It is the one complete training cycle. 
- Epoch 10: Model has seen all images 10 times 
- More epochs generally improve learning, but too many may cause overfitting.
# 5. What is best.pt? 
best.pt is the best-performing trained model saved during training.