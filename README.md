👁️‍🗨️ Face Recognition Script (Real-time with Webcam)
This Python script uses the face_recognition library in combination with OpenCV to perform real-time face recognition using your system's webcam. It compares faces from a live webcam stream against a set of pre-encoded known faces.

🧠 How It Works
Load & Encode Known Faces:

The script loads image files of known individuals from the faces/ directory.

Each image is encoded using face_recognition.face_encodings(), producing a unique 128-d facial feature vector.

Capture Live Video:

Accesses the default webcam using cv2.VideoCapture(0).

Detect Faces in Real-Time:

Each frame is resized and converted to RGB.

Faces are detected and encoded using the same encoding algorithm.

Compare with Known Faces:

The live face encodings are compared with known face encodings using:

face_recognition.compare_faces(): Boolean match.

face_recognition.face_distance(): Distance score (lower is better).

The best match is selected using np.argmin().

Display the Match:

If a match is found, the name is overlayed on the video feed using cv2.putText().

Exit Mechanism:

Press q to quit the application.

📂 Directory Structure
bash
Copy
Edit
FaceRecognition/
├── recognizer.py             # Main script (your current code)
├── faces/
│   ├── 1706628890587.jpg     # Face of 'shreyansh'
│   ├── tapish.jpg            # Face of 'tapish'
│   ├── bhargav.jpg           # Face of 'devansh'
│   └── tare.jpg              # Face of 'aditya'
└── README.md                 # Documentation file
🛠 Requirements
Python 3.6+

OpenCV (cv2)

face_recognition (uses dlib)

NumPy

Install dependencies via pip:

bash
Copy
Edit
pip install opencv-python face_recognition numpy
Note: On Windows, installing dlib might require Visual Studio Build Tools. You can use prebuilt wheels for convenience.

▶️ How to Run
bash
Copy
Edit
python recognizer.py
The webcam feed will open and start matching detected faces against the known dataset. The recognized person's name will appear on the screen. Press q to exit.

🧑‍💻 Code Overview
python
Copy
Edit
# Load and encode known faces
shr_encoding = face_recognition.face_encodings(face_recognition.load_image_file("faces/1706628890587.jpg"))[0]
...
known_face_encodings = [shr_encoding, tare_encoding, ...]
known_face_names = ["shreyansh", "aditya", ...]

# Start webcam and begin frame-by-frame recognition
video_capture = cv2.VideoCapture(0)
...
for face_encoding in face_encodings:
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    ...
🔒 Limitations
Works best in well-lit environments.

Doesn't handle multiple faces efficiently if lighting and angle vary drastically.

No error handling if face encodings fail or camera access fails.

🚀 Future Improvements
Draw bounding boxes around faces.

Add GUI for managing known faces.

Improve accuracy using image augmentation.

Add logging or authentication features.
