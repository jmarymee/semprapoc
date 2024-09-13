import cv2

# RTSP stream URL
rtsp_url = "rtsp://192.168.0.146:8554/stream"

# Open the RTSP stream
cap = cv2.VideoCapture(rtsp_url)

# Check if the stream is opened successfully
if not cap.isOpened():
    print("Failed to open RTSP stream")
    exit()

# Read and display frames from the stream
while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to read frame from RTSP stream")
        break

    cv2.imshow("RTSP Stream", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()