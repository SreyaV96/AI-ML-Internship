## 1. Explain the complete YOLO workflow.
```text
Problem Identification
        ↓
Data Collection
        ↓
Data Annotation
        ↓
Dataset Preparation
        ↓
Create data.yaml
        ↓
Load YOLO Model
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Save Best Model (best.pt)
        ↓
Testing
        ↓
Deployment
```
#### Explanation
- Problem Identification: Define the objective (e.g., detect workers wearing helmets and not wearing helmets).
- Data Collection: Gather images containing object (e.g.,helmet and no-helmet cases).
- Data Annotation: Draw bounding boxes and assign class labels using tools such as LabelImg or Roboflow
- Dataset Preparation: Split data into train, validation, and test sets.
- Create data.yaml: Configure dataset paths and class names.
- Model Training: Train YOLO using annotated images.
- Model Evaluation: Measure performance using Precision, Recall, and mAP.
- Save Best Model: Store the highest-performing model as best.pt.
- Testing: Test on unseen images.
- Deployment: Integrate the trained model into a real-world application such as CCTV monitoring.
## 2. Why is annotation important? 
Annotation is the process of marking objects in images using bounding boxes and labels.
#### Importance
- Provides ground-truth information for training.
- Helps YOLO learn object location and class.
- Improves detection accuracy.
- Enables the model to distinguish between different classes.
## 3. What is best.pt? 
- best.pt is the best-performing trained model generated during YOLO training. 
- It Contains the weights of the model that achieved the best validation performance. 
- Selected automatically based on evaluation metrics
- used for testing and deployment.
## 4. What is deployment? 
Deployment is the process of using the trained model in a real-world environment.
#### Examples
- CCTV camera monitoring
- Construction site safety systems
- Live webcam detection
- Industrial safety monitoring
## 5. Explain the role of data.yaml. 
- data.yaml is a configuration file used by YOLO to describe the dataset.
- It tells the model:
    - Where training images are stored
    - Where validation images are stored
    - Number of classes
    - class names
#### Example
train: dataset/images/train
val: dataset/images/val

nc: 2

names:
  0: Helmet
  1: No_Helmet