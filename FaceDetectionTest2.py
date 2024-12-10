import cv2
import mediapipe as mp
import time
import yt_dlp
import os

# Step 1: Define directories
youtube_download_dir = "youtube_download_content"
output_video_dir = "output_video"

# Create directories if they don't exist
os.makedirs(youtube_download_dir, exist_ok=True)
os.makedirs(output_video_dir, exist_ok=True)

# Define paths
youtube_video_path = os.path.join(youtube_download_dir, "downloaded_video.mp4")
output_video_path = os.path.join(output_video_dir, "processed_video.mp4")

# Step 2: Download YouTube video
def download_youtube_video(url, output_path):
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

url = "https://www.youtube.com/shorts/FAzchrNh8eI"
print(f"Downloading video from: {url}")
download_youtube_video(url, youtube_video_path)
print(f"Video downloaded to: {youtube_video_path}")

# Step 3: Initialize MediaPipe and OpenCV
cap = cv2.VideoCapture(youtube_video_path)
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.85)

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define video writer for output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

print(f"Processing video and saving output to: {output_video_path}")

# Step 4: Process video and save frames
while True:
    success, img = cap.read()
    if not success:
        print("Video processing completed!")
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)

    if results.detections:
        for id, detection in enumerate(results.detections):
            mpDraw.draw_detection(img, detection)
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = (int(bboxC.xmin * iw), int(bboxC.ymin * ih),
                    int(bboxC.width * iw), int(bboxC.height * ih))
            cv2.rectangle(img, bbox, (255, 0, 255), 2)
            cv2.putText(img, f'{int(detection.score[0] * 100)}%',
                        (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2,
                        (255, 0, 255), 2)

    cTime = time.time()
    if cTime != pTime:
        fps_display = 1 / (cTime - pTime)
    else:
        fps_display = 0  # Avoid division by zero

    #fps_display = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps_display)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (0, 255, 0), 2)

    # Write frame to output video
    out.write(img)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Output video saved to: {output_video_path}")
