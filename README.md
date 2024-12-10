# YouTube Face Detection with AI  
🚀 **Real-Time Face Detection on YouTube Videos using Python**  

This project demonstrates **real-time face detection** on a YouTube video by leveraging **MediaPipe** and **OpenCV**. The system processes videos sourced from YouTube, detects faces with bounding boxes, and saves the processed video to a local folder.

---

## 📂 **Project Overview**  
- Download and process YouTube videos using `pytube`.  
- Detect faces in each frame using **MediaPipe Face Detection**.  
- Save the processed output video in the `output_video` folder.  
- Designed for learners and developers exploring **computer vision** and **AI-powered applications**.

---

## 🛠️ **Tech Stack**  
- **Python**  
- **MediaPipe** for face detection  
- **OpenCV** for video processing  
- **Pytube** for downloading YouTube videos  

---

## 📁 **Folder Structure**  
```plaintext
.
├── FaceDetectionTest.py          # Main script for processing
├── youtube_download_content      # Folder for downloaded videos
├── output_video                  # Folder for processed videos
├── requirements.txt              # Dependencies for the project
└── README.md                     # Project documentation


 🖥️ How to Run the Project  

1. Clone this repository:  
   ```bash
   git clone https://github.com/jayambe36/YouTube-Face-Detection-AI.git
   cd YouTube-Face-Detection-AI

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows  
    source venv/bin/activate  # macOS/Linux

3. Install dependencies:

    ```bash
    pip install -r requirements.txt

4. Run the project
    python FaceDetectionTest.py

📹 Video Demo
Downloaded YouTube videos are saved in the youtube_download_content folder. Processed videos with face detection are saved in the output_video folder.

🔗 Features
Process videos from YouTube directly via URL.

Efficient face detection with bounding boxes and confidence scores.

Save both downloaded and processed videos for further analysis.

📝 Requirements
Python 3.8+

Install dependencies using the provided requirements.txt file.

📧 Contact & Contributions
Feel free to raise issues or contribute to this project by submitting pull requests.

📩 Contact: smitrpatel19@gmail.com

⭐ Don't forget to star this repository if you find it helpful!