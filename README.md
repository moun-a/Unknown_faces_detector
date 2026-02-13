## AI Surveillance System – Face Recognition Alert

Real-time intelligent surveillance system using DeepFace, OpenCV, and Telegram API.
The system detects faces via webcam, recognizes known individuals from a local database, and sends an alert if an unknown person is detected.

## Features

🎥 Real-time face detection using webcam

🧠 Face recognition using VGG-Face model

📂 Local face database (faces_db)

🚨 Alert triggered after multiple consecutive unknown detections

📲 Automatic Telegram alert with captured image

🛑 Alert interval control to prevent spam

🖥 Live display with detected person name

## Technologies Used

- Python 3

- OpenCV

- DeepFace

- VGG-Face Model

- Telegram Bot API

- Requests Library

## Project Structure
EcoCold/

│

├── main.py                # Main face recognition script

├── faces_db/              # Folder containing known faces

│     ├── person1.jpg

│     ├── person2.jpg

│
├── demo/                  # Screenshots and demo results

│     ├── screenshot1.png

│     ├── test_result.png

│

└── README.md

## Installation
1️⃣ Clone the repository
git clone https://github.com/moun-a/Unknown_faces_detector.git
cd your-repository

2️⃣ Install dependencies
pip install opencv-python deepface requests

 ## Configuration

Inside main.py, configure:

DB_PATH = "faces_db"
MODEL_FACE = "VGG-Face"
DETECTOR = "opencv"
ALERT_INTERVAL = 10
TOLERANCE_COUNT = 3
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_IDS = ["CHAT_ID_1", "CHAT_ID_2"]

## Telegram Setup

Create a bot using @BotFather

Copy the Bot Token

Get your Chat ID

Replace values in the script

## How It Works

Webcam captures frames in real time.

Each frame is analyzed using DeepFace.

If a known face is detected → name is displayed.

If an unknown face appears for multiple consecutive frames:

An alert image is captured

Telegram notification is sent

Alert interval prevents repeated spam.

## Detection Logic

TOLERANCE_COUNT: Number of consecutive "Unknown" frames before triggering alert.

ALERT_INTERVAL: Minimum seconds between two alerts.

enforce_detection=False: Prevents crashes if no face detected.

## Demo

Demo images are available in the demo/ folder.

Example alert:

🚨 Alerte ! Visage détecté : Inconnu

🔐 Security Notes

⚠️ Do NOT upload your Telegram Bot Token publicly.
Consider using environment variables for production:

export TELEGRAM_BOT_TOKEN=your_token

##  Future Improvements

Add face bounding boxes

Add face tracking

Deploy on Raspberry Pi

Add database logging

Connect to web dashboard

Use GPU acceleration

## Author

Mouna MOUHIB
Embedded Systems & Digital Services Engineering Student
Interested in IoT, AI, and Intelligent Surveillance Systems

## License

This project is open-source and available for educational and research purposes.
