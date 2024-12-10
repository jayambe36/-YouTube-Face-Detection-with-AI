import cv2
import mediapipe as mp
import time
import yt_dlp
import os

# Step 1: Download the YouTube video
url = "https://www.youtube.com/shorts/FAzchrNh8eI"
download_path = "youtube_video.mp4"

def download_youtube_video(url, output_path):
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

print(f"Downloading video from: {url}")
download_youtube_video(url, download_path)
print(f"Video downloaded to: {download_path}")

# Step 2: Initialize OpenCV and MediaPipe
cap = cv2.VideoCapture(download_path)
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.85)

# Step 3: Process the video frame by frame
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
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (0, 255, 0), 2)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Step 4: Clean up the downloaded video (optional)
#os.remove(download_path)
#print(f"Temporary video file '{download_path}' deleted.")
