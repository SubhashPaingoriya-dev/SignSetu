import cv2
import mediapipe as mp
import time

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

BaseOptions = python.BaseOptions
GestureRecognizer = vision.GestureRecognizer
GestureRecognizerOptions = vision.GestureRecognizerOptions
VisionRunningMode = vision.RunningMode

options = GestureRecognizerOptions(
    base_options=BaseOptions(
        model_asset_path="../model/gesture_recognizer.task"
    ),
    running_mode=VisionRunningMode.VIDEO
)

recognizer = GestureRecognizer.create_from_options(options)

cap = cv2.VideoCapture(0)

sentence = ""
current_letter = ""
last_add_time = time.time()

timestamp = 0

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=frame
    )

    timestamp += 1

    result = recognizer.recognize_for_video(mp_image, timestamp)

    if result.gestures:

        gesture = result.gestures[0][0].category_name

        # use specific gestures
        if gesture == "Thumb_Up":
            if current_letter != "":
                sentence += current_letter
                current_letter = ""

        elif gesture == "Closed_Fist":
            sentence += " "

        else:
            current_letter = gesture

        cv2.putText(frame,f"Gesture: {gesture}",(50,50),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.putText(frame,f"Word: {sentence}",(50,120),
                cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

    cv2.imshow("SignConnect",frame)

    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()