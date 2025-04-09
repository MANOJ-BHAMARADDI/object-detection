import cv2
from ultralytics import YOLO
import time

# Load pre-trained YOLOv8 nano model
model = YOLO("yolov8n.pt")  # You uploaded this!

# Start video capture (0 = default webcam)
cap = cv2.VideoCapture(0)

# Set video resolution (optional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)


cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        start_time = time.time()

        # Inference
        results = model.predict(source=frame, conf=0.5, verbose=False)[0]
        annotated_frame = results.plot()

        # Show FPS
        end_time = time.time()
        fps = 1 / (end_time - start_time)
        cv2.putText(annotated_frame, f"FPS: {fps:.2f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display the result
        cv2.imshow("YOLOv8 - Phone Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

except KeyboardInterrupt:
    print("Stopped by user.")

finally:
    cap.release()
    cv2.destroyAllWindows()
