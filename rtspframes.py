import cv2
import time

def capture_frames(rtsp_url, output_dir):
    cap = cv2.VideoCapture(rtsp_url)
    frame_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_count % 5 == 0:
            timestamp = int(time.time())
            filename = f"{output_dir}/frame_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Saved frame {frame_count} as {filename}")

        frame_count += 1
        time.sleep(1)

    cap.release()

# Example usage
rtsp_url = "rtsp://192.168.0.146/stream"
output_dir = "./frames"
capture_frames(rtsp_url, output_dir)