# 1. What is Computer Vision? 
Computer Vision (CV) is a field of Artificial Intelligence (AI) that enables computers to interpret, analyze, and understand images and videos similarly to human vision.

- It involves tasks such as:
    - Image Classification
    - Object Detection
    - Face Recognition
    - Image Segmentation
    - Motion Tracking
    - Medical Image Analysis

- Example: A self-driving car identifying roads, traffic signs, pedestrians, and vehicles.
# 2. What is Object Detection? 
Object Detection is a computer vision technique used to identify and locate objects within an image or video.
It performs two tasks:

1. Classification – Determines what the object is.
2. Localization – Determines where the object is located.

- Example:
In a street image, object detection can identify:
    - Car
    - Person
    - Bicycle
    - Traffic Light and draw boxes around them.

# 3. What is YOLO? 
- YOLO (You Only Look Once) is a real-time object detection algorithm.
- Unlike traditional methods that scan an image multiple times, YOLO processes the entire image in a single pass, making it extremely fast.
#### Key Features

- Real-time detection
- High accuracy
- Single neural network architecture
- Detects multiple objects simultaneously

#### YOLO Workflow

1. Input image
2. Neural network analyzes image
3. Predicts object classes
4. Predicts bounding boxes
5. Outputs detected objects

# 4. What is a Bounding Box? 
- A Bounding Box is a rectangular box drawn around an object detected in an image.

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


# 5. Advantages of YOLO? 
#### 1. High Speed

- Processes images in real time.
- Suitable for video streams.

#### 2. Single-Pass Detection

- Looks at the image only once.
- Faster than many older methods.

#### 3. Detects Multiple Objects

- Can find several objects simultaneously.

#### 4. Good Accuracy

- Provides strong detection performance.

#### 5. End-to-End Training

- Easy to train and deploy.

#### 6. Works on Videos

- Ideal for surveillance and autonomous systems.

#### 7. Low Latency

- Quick predictions with minimal delay.

#### 8. Scalable Models

- Different model sizes for different hardware.
