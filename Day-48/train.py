from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data=r"D:\AI-ML-Internship\Day-48\helmet_detection_dataset\data.yaml",
    epochs=10,
    imgsz=512,
    batch=4,
    workers=0,
    amp=False,
    plots=False,
    project=r"D:\AI-ML-Internship\Day-48\runs\detect",
    name="train"
)
