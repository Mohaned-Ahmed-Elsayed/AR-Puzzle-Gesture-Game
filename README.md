# 🎮 AR Puzzle Game with Gesture Control

An **Augmented Reality Puzzle Game** controlled entirely by hand gestures, built with **MediaPipe**, **OpenCV**, and a trained **KNN classifier with PCA**.

Players pinch, open, and move puzzle tiles to solve a sliding puzzle in real time — no mouse or keyboard required.

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Features

- 🖐️ Real-time hand tracking with MediaPipe
- 🧠 Gesture classification using PCA + KNN
- 🧩 Interactive sliding puzzle controlled by pinch/open gestures
- 🎯 Confidence filtering for robust, jitter-free predictions
- ✅ Reset and win conditions with visual feedback

---

## 🎥 Demo

> *(Add a GIF or screenshot of the game in action here)*

---

## 📂 Project Structure

```
project-root/
│
├── config/
│   └── settings.py           # Global constants (camera size, grid size, gestures)
│
├── core/
│   ├── camera.py              # Camera input wrapper
│   ├── hand_tracker.py        # Hand tracking + gesture detection
│   ├── gesture_classifier.py  # Classifier for gestures
│   ├── evaluator.py           # Evaluation metrics
│   ├── pca_model.py           # PCA transformer loader
│   └── utils.py                # Helper functions (distance, etc.)
│
├── game/
│   ├── puzzle.py               # Puzzle logic
│   ├── controller.py           # Gesture-based puzzle controller
│   └── renderer.py             # Puzzle rendering on screen
│
├── data/
│   ├── collect_data.py         # Script to collect gesture data
│   ├── train_model.py          # Train PCA + KNN classifier
│   └── dataset.csv              # Created automatically when collecting data
│
├── models/                      # Saved models (created after training)
│   ├── pca.pkl
│   └── classifier.pkl
│
└── main.py                      # Entry point for the AR puzzle game
```

---

## ⚙️ Installation

**Requirements:** Python 3.9+, a webcam

```bash
git clone https://github.com/USERNAME/REPO_NAME.git
cd REPO_NAME

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

---

## 📊 Usage

### 1. Collect gesture data

```bash
python data/collect_data.py
```

Perform gestures (pinch, open, fist) in front of the camera and press `q` to stop. This creates or updates `data/dataset.csv`.

### 2. Train the model

```bash
python data/train_model.py
```

Splits the dataset into train/test sets, applies PCA, trains the KNN classifier, and saves the resulting models into `models/`.

### 3. Run the game

```bash
python main.py
```

| Gesture | Action |
|---|---|
| Pinch + drag | Select a region of interest (ROI) for the puzzle image |
| Release fingers | Confirm the selected puzzle image |
| Pinch | Pick up and move a tile |
| Open hand | Reset the puzzle |

Solve the puzzle to win! 🏆

---

## 🛠️ Tech Stack

- **[MediaPipe](https://developers.google.com/mediapipe)** — hand landmark detection
- **[OpenCV](https://opencv.org/)** — camera input and rendering
- **[scikit-learn]** — PCA dimensionality reduction + KNN classification

---

## 🗺️ Roadmap

- [ ] Support for multiple puzzle sizes (3x3, 4x4, 5x5)
- [ ] Additional gesture vocabulary (swipe, rotate)
- [ ] On-screen calibration wizard for new users

---
## 👤 Author

**Mohaned Ahmed Elsayed**  
- LinkedIn: [linkedin.com/in/mohanedahmed1](https://linkedin.com/in/mohanedahmed1)  
- GitHub: [github.com/Mohaned-Ahmed-Elsayed](https://github.com/Mohaned-Ahmed-Elsayed)

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
