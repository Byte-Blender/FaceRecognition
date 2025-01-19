import cv2
import face_recognition
import numpy as np
import time



def recognizer():
    global name
    i = 1
    video_capture = cv2.VideoCapture(0)
    # image and their encoding
    shr_image = face_recognition.load_image_file(r"faces/1706628890587.jpg")
    shr_encoding = face_recognition.face_encodings(shr_image)[0]

    tapish_image = face_recognition.load_image_file(r"faces/tapish.jpg")
    tapish_encoding = face_recognition.face_encodings(tapish_image)[0]

    bhargav_image = face_recognition.load_image_file(r"faces/bhargav.jpg")
    bhargav_encoding = face_recognition.face_encodings(bhargav_image)[0]

    tare_image = face_recognition.load_image_file(r"faces/tare.jpg")
    tare_encoding = face_recognition.face_encodings(tare_image)[0]

    known_face_encodings = [shr_encoding, tare_encoding, tapish_encoding, bhargav_encoding]

    known_face_names = ["shreyansh", "aditya", "tapish", "devansh"]

    people = known_face_names.copy()

    face_locations = []
    face_encodings = []





    while True:

        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:

                name = known_face_names[best_match_index]
            else:
                continue

            if name in known_face_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 100)
                fontScale = 1.5
                fontColor = (255, 0, 0)
                thickness = 3
                lineType = 2
                cv2.putText(frame, name, bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

        cv2.imshow("person", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


    video_capture.release()
    cv2.destroyAllWindows()

    return name
recognizer()