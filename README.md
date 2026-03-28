<div align="center">

<img src="https://img.shields.io/badge/SignSetu-AI%20Powered-blueviolet?style=for-the-badge&logo=hand&logoColor=white" alt="SignSetu"/>

# 🤝 SignSetu
### AI-Powered Hand Gesture Communication System

> **"Setu" means Bridge** — SignSetu bridges the communication gap for speech and hearing impaired users.

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-00897B?style=flat-square&logo=google&logoColor=white)](https://mediapipe.dev)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=flat-square&logo=react&logoColor=black)](https://reactjs.org)


<br/>

**SignSetu** is an AI-based real-time web application that lets speech & hearing impaired users communicate using hand gestures — translated instantly into text and voice output.

[🚀 Demo](#-demo) · [📦 Installation](#-installation) · [🧠 How It Works](#-how-it-works) · [✨ Features](#-features) · [📸 Screenshots](#-screenshots)

---

</div>

## 📌 Table of Contents

- [🌟 What is SignSetu?](#-what-is-signsetu)
- [🚀 How It Works](#-how-it-works)
- [🧠 Machine Learning Architecture](#-machine-learning-architecture)
- [🎨 Frontend Interface](#-frontend-interface)
- [🔊 Text-to-Speech](#-text-to-speech)
- [✨ Features](#-features)
- [👤 User Workflow](#-user-workflow)
- [🏗️ Tech Stack](#️-tech-stack)
- [📁 Project Structure](#-project-structure)
- [📦 Installation](#-installation)
- [🎯 Target Users](#-target-users)
- [💡 Why SignSetu?](#-why-signsetu)
- [📸 Screenshots](#-screenshots)

---

## 🌟 What is SignSetu?

SignSetu is an **adaptive, real-time gesture communication system** that empowers non-verbal users to communicate effortlessly. Using your device's camera, SignSetu detects hand gestures, predicts letters through AI, builds sentences, and converts them into voice output — all in real-time, with no keyboard needed.

```
Hand Gesture  →  AI Detects Letter  →  User Confirms 👍  →  Sentence Built  →  🔊 Voice Output
```

---

## 🚀 How It Works

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│   📷 Camera Input                                            │
│         ↓                                                    │
│   🖐 MediaPipe Hand Landmark Detection                       │
│         ↓                                                    │
│   📐 63 Feature Points Extracted (x, y, z)                  │
│         ↓                                                    │
│   🤖 ML Classifier (RandomForest / MLP)                     │
│         ↓                                                    │
│   🔤 Letter Prediction   →   e.g., "H"                      │
│         ↓                                                    │
│   👍 User Confirms Gesture                                   │
│         ↓                                                    │
│   📊 Dataset Updated  +  Model Retrains                     │
│         ↓                                                    │
│   📝 Sentence Formed  →  "HELLO WORLD"                      │
│         ↓                                                    │
│   🔊 Text-to-Speech Voice Output                            │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 🧠 Machine Learning Architecture

SignSetu uses a **Human-in-the-Loop** machine learning approach, meaning the AI learns and improves from every interaction with the user.

### Model Pipeline

| Stage | Technology | Description |
|-------|-----------|-------------|
| 📷 Input | Webcam API | Captures real-time video frames |
| ✋ Detection | MediaPipe | Detects hand presence and 21 landmarks |
| 📐 Feature Extraction | NumPy | Extracts 63 points (x, y, z per landmark) |
| 🤖 Classification | scikit-learn | RandomForest / MLP predicts the gesture |
| ✅ Confirmation | UI Gesture (👍) | User validates prediction accuracy |
| 📊 Training | Incremental | Dataset grows; model retrains automatically |

### ML Techniques Used

- 🔍 **Computer Vision** — MediaPipe for real-time hand landmark detection
- 🎓 **Supervised Learning** — Trained classifier on labeled gesture data
- 🔄 **Human-in-the-Loop** — User feedback improves model accuracy
- ⚡ **Real-Time Inference** — Predictions made at every frame
- 📈 **Incremental Learning** — Model improves continuously with use

### Why This ML Approach?

> Traditional sign language apps use fixed datasets. SignSetu is **different**:

| Traditional Apps | SignSetu |
|-----------------|---------|
| Fixed dataset | Grows with every user |
| Generic model | Personalized to YOUR hand |
| No improvement | Improves over time |
| One-size-fits-all | Adaptive AI |

---

## 🎨 Frontend Interface

The UI is clean, accessible, and gesture-driven — no keyboard or mouse required.

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   ┌───────────────────┐   Prediction: [ H ]         │
│   │                   │                             │
│   │    📷 CAMERA      │   Sentence:                 │
│   │       BOX         │   ┌─────────────────────┐   │
│   │                   │   │  H E L L O  W O R L D  │
│   └───────────────────┘   └─────────────────────┘  │
│                                                     │
│   Gesture Controls:        [ 🔊 Speak ]             │
│   👍  Confirm Letter                                │
│   ✊  Add Space                                     │
│   🖐  Clear Sentence                               │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### UI Components

| Component | Description |
|-----------|-------------|
| 📷 **Camera Box** | Live feed where user shows gestures |
| 🔤 **Prediction Panel** | Displays the AI-predicted letter in real-time |
| 📝 **Sentence Builder** | Accumulates confirmed letters into words |
| 🖐 **Gesture Guide** | Visual reference for control gestures |
| 🔊 **Speak Button** | Converts built sentence to AI voice |

---

## 🔊 Text-to-Speech

After the user builds a sentence using gestures, SignSetu converts it to voice:

```
User signs:   H → E → L → L → O
              ↓
Sentence:     "HELLO"
              ↓
AI Voice:     🔊 "Hello"
```

### TTS Technologies Supported

- 🌐 **Web Speech API** — Browser-native, no installation required
- 🐍 **pyttsx3** — Offline Python TTS engine
- ☁️ **gTTS (Google TTS)** — High-quality online voice synthesis

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎯 **Live AI Prediction** | Real-time letter detection from hand gestures |
| 👍 **Confirmation Gesture** | Thumbs-up to approve a prediction — user stays in control |
| 📝 **Auto Sentence Builder** | Confirmed letters automatically form words and sentences |
| 🔊 **Text-to-Speech** | Converts typed sentence to spoken voice output |
| 🧠 **Adaptive AI Training** | Model learns your gestures and improves over time |
| ✊ **Space Gesture** | Fist gesture adds a word space |
| 🖐 **Clear Gesture** | Open palm clears the entire sentence |
| 📴 **No Keyboard Needed** | Fully gesture-driven interface |
| 🔒 **Personalized Model** | AI adapts specifically to the user's hand shape & style |

---

## 👤 User Workflow

Here's exactly how a user communicates using SignSetu:

**Step 1 — Open the App**
```
Open SignSetu in browser → Camera starts automatically
```

**Step 2 — Show a Gesture**
```
User shows hand gesture inside the camera box
Example: sign the letter "H"
```

**Step 3 — AI Predicts**
```
Prediction: H
```

**Step 4 — Confirm with 👍**
```
User gives thumbs-up → "H" is added to sentence
```

**Step 5 — Continue Signing**
```
H → E → L → L → O
```

**Step 6 — Speak**
```
User clicks [ 🔊 Speak ]
AI voice says: "Hello"
✅ Communication complete!
```

---

## 🏗️ Tech Stack

### Machine Learning
```
Python 3.8+        — Core language
MediaPipe          — Hand landmark detection
scikit-learn       — ML classifier (RandomForest / MLP)
NumPy              — Feature extraction & data handling
```

### Frontend
```
React / HTML CSS JS   — UI framework
Webcam API            — Real-time camera access
Web Speech API        — Browser-native TTS
```

### AI Features
```
Gesture Recognition   — Real-time hand pose classification
Online Training       — Human-in-the-loop model updates
Text Generation       — Sentence building from gestures
Speech Synthesis      — Multi-engine TTS output
```

---

## 📁 Project Structure

```
SignSetu/
│
├── 📂 model/
│   ├── gesture_model.pkl          # Trained ML classifier
│   ├── hand_landmarker.task       # MediaPipe hand detection model
│   └── gesture_recognizer.task   # Gesture recognition task file
│
├── 📂 src/
│   ├── predict_final.py           # Real-time prediction script
│   ├── train.py                   # Model training script
│   └── collect.py                 # Gesture data collection
│
├── 📂 frontend/
│   ├── index.html                 # Main UI entry point
│   ├── app.js / App.jsx           # React app or vanilla JS
│   └── styles.css                 # UI styling
│
├── 📄 README.md                   # Project documentation
└── 📄 requirements.txt            # Python dependencies
```

---

## 📦 Installation

### Prerequisites

- Python 3.8 or above
- Node.js (if using React frontend)
- A working webcam

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/SignSetu.git
cd SignSetu
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Key Python Packages

```bash
pip install mediapipe scikit-learn numpy opencv-python pyttsx3
```

### 4. Collect Gesture Data

```bash
python src/collect.py
```

### 5. Train the Model

```bash
python src/train.py
```

### 6. Run Prediction

```bash
python src/predict_final.py
```

### 7. Launch the Frontend

```bash
# For plain HTML/CSS/JS
open frontend/index.html

# For React
cd frontend
npm install
npm start
```

---

## 🎯 Target Users

| User Group | How SignSetu Helps |
|------------|-------------------|
| 🧏 **Deaf Users** | Communicate through gestures without audio |
| 🤐 **Mute Users** | Express thoughts via AI-generated voice |
| 🏥 **Medical Recovery Patients** | Communicate during speech recovery |
| 🎓 **Special Education Students** | Alternative communication tool |
| 🗣️ **Speech Impaired** | Real-time gesture-to-speech conversion |

---

## 💡 Why SignSetu?

> SignSetu is not just another sign language app — it's a **personalized, adaptive AI** built around the user.

```
❌ Most Apps        ✅ SignSetu
─────────────────────────────────────
Fixed dataset    →  Grows with you
Generic model    →  Learns your hand
No improvement   →  Gets smarter daily
Keyboard needed  →  100% gesture-driven
One-time setup   →  Continuous learning
```

---

## 📸 Screenshots

> 📷 *Screenshots and demo GIFs will be added here after deployment.*

### Camera & Prediction View
```
[ Screenshot: Live camera feed with hand gesture and AI prediction panel ]
```

### Sentence Builder
```
[ Screenshot: Built sentence "HELLO WORLD" displayed in the output panel ]
```

### Gesture Guide Panel
```
[ Screenshot: Visual guide showing 👍 Confirm, ✊ Space, 🖐 Clear gestures ]
```

### Text-to-Speech in Action
```
[ Screenshot or GIF: Speak button clicked, voice output indicator active ]
```

### Adaptive Training Flow
```
[ Screenshot: Training confirmation after thumbs-up gesture, model update notification ]
```

> 💡 **Tip:** Replace the placeholder blocks above with actual screenshots from your app. Recommended size: **1280×720px** or **1920×1080px**.
>
> To add images, upload them to your repo and use:
> ```markdown
> ![Description](screenshots/your-image.png)
> ```

---

## 🏷️ Resume Description

> *Copy-paste ready for your resume or LinkedIn:*

**SignSetu — AI Powered Hand Gesture Communication System**
Developed a real-time AI communication system for speech-impaired users using MediaPipe hand tracking, scikit-learn ML classifier, and human-in-the-loop adaptive training. Implemented gesture confirmation, auto sentence building, and text-to-speech output — enabling fully gesture-driven communication without any keyboard or physical input device.

---

<div align="center">

Made with ❤️ to bridge the communication gap

⭐ **Star this repo if you find it useful!**

</div>
