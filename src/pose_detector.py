import cv2
import mediapipe as mp
from utils import open_spotify_windows, close_spotify_windows

# Initialize MediaPipe
mp_face = mp.solutions.face_detection
mp_hands = mp.solutions.hands

face_detector = mp_face.FaceDetection(min_detection_confidence=0.6)
hands_detector = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

# Webcam setup
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # CAP_DSHOW helps on Windows
pose_active = False

print("▶ Pose like the Blonde cover... (Press 'q' to quit)")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ ERROR: Camera frame not received. Check webcam.")
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_results = face_detector.process(rgb)
    hand_results = hands_detector.process(rgb)

    pose_now = False

    if face_results.detections and hand_results.multi_hand_landmarks:
        face_box = face_results.detections[0].location_data.relative_bounding_box
        fx, fy = int(face_box.xmin * w), int(face_box.ymin * h)
        fw, fh = int(face_box.width * w), int(face_box.height * h)
        forehead_y = fy - 20
        forehead_x1, forehead_x2 = fx, fx + fw

        for hand_landmarks in hand_results.multi_hand_landmarks:
            for lm in hand_landmarks.landmark:
                x, y = int(lm.x * w), int(lm.y * h)
                if forehead_x1 < x < forehead_x2 and forehead_y - 40 < y < forehead_y + 60:
                    pose_now = True
                    break

    if pose_now and not pose_active:
        open_spotify_windows()
        pose_active = True
    elif not pose_now and pose_active:
        close_spotify_windows()
        pose_active = False

    if pose_active:
        cv2.putText(
            frame,
            "Certified Blonded",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.5,
            (255, 255, 255),
            3,
            cv2.LINE_AA
        )

    cv2.imshow("Frank Ocean Pose Detector", frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
close_spotify_windows()
