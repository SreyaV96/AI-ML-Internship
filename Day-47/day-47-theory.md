# 1. What is Video Object Detection? 
Video Object Detection is the process of identifying and locating objects in each frame of a video. The system detects objects such as people, cars, bicycles, and animals, and draws bounding boxes around them while the video is playing.
#### Example:
 - Traffic Monitoring
 - CCTV Surveillance 

# 2. What is Real-Time Detection? 
- Real-Time Detection refers to detecting objects instantly as video frames are captured from a camera or webcam, with minimal delay.
- The processing speed is usually measured in Frames Per Second (FPS).
### Applications:
 - Security surveillance
 - Autonomous vehicles
 - Face recognition systems
 - Smart traffic monitoring
# 3. What is OpenCV? 
- OpenCV (Open Source Computer Vision Library) is an open-source library used for computer vision and image processing tasks.
- It helps us: 
    - Read Images 
    - Read Videos 
    - Access Webcam 
    - Process Frames 
# 4. Why is YOLO suitable for video detection? 
- Very fast detection speed
- Processes entire image in a single pass
- Works well for real-time applications
- High accuracy
- Can detect multiple objects simultaneously

# 5. What does VideoCapture(0) mean? 
In OpenCV, `VideoCapture(0)` is used to access the computer's default webcam.

### Syntax

```python
cap = cv2.VideoCapture(0)
```
- cv2.VideoCapture() is an OpenCV function used to capture video.
- The number 0 represents the first (default) camera connected to the system.
- If multiple cameras are connected:
    - 0 → First camera
    - 1 → Second camera
    - 2 → Third camera