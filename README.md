# 👁️ Face Recognition System

This is a **Python-based real-time Face Recognition System** using a webcam feed. It detects and identifies known faces using the `face_recognition` and `OpenCV` libraries. The system is ideal for building security or identity verification systems.

---

## 📸 Features

- 🔍 Detects and recognizes faces from webcam feed  
- 🎯 Matches faces against a preloaded database of known individuals  
- 🧠 Uses deep learning-based face encoding and comparison  
- 🖥️ Displays the recognized name in real-time on screen  
- ⏹️ Press `q` to quit the application  

---

## 📂 Project Structure

FaceRecognition/ ├── recognizer.py # Main face recognition script ├── faces/ # Folder containing reference face images │ ├── 1706628890587.jpg # Image for 'shreyansh' │ ├── tapish.jpg # Image for 'tapish' │ ├── bhargav.jpg # Image for 'devansh' │ └── tare.jpg # Image for 'aditya' └── README.md # Project documentation (this file)

yaml
Copy
Edit

---

## 🛠️ Requirements

Ensure you have Python 3.6+ installed. Then install the dependencies:

```bash
pip install face_recognition opencv-python numpy
⚠️ On Windows, face_recognition may require dlib with CMake and Visual Studio Build Tools installed.

▶️ How to Run
bash
Copy
Edit
python recognizer.py
The webcam will open.

The system will try to recognize any faces seen in the webcam.

If a known face is detected, the name will appear on the frame.

Press q to close the video window and exit the script.

🧠 How It Works
Loads known face images from the faces/ directory.

Encodes each known face using a 128-dimensional embedding.

Captures frames from the webcam.

Detects and encodes faces in each frame.

Compares these encodings with the known encodings.

If matched, displays the corresponding name on the screen.

💡 Code Highlights
python
Copy
Edit
matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
best_match_index = np.argmin(face_distance)
if matches[best_match_index]:
    name = known_face_names[best_match_index]
🔒 Limitations
Works best with good lighting and front-facing faces

Accuracy may decrease for side faces or occlusions

Faces not in the database will be ignored

🚀 Future Improvements
Draw rectangles around faces

Add face registration GUI

Store face encodings in a database or file

Support for multiple camera feeds

📄 License
This project is licensed under the MIT License. You are free to use, modify, and distribute it for personal or commercial use.

🙌 Acknowledgements
face_recognition

OpenCV

yaml
Copy
Edit
