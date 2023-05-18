import cv2
import math
import mediapipe as mp
import interface
label = None
new_label = None

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.6)
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# refer to https://google.github.io/mediapipe/images/mobile/hand_landmarks.png for landmark reference
# 4, 8, 12, 16, 20 are the tips of each finger
mediapipe_tip_id = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    h, w, c = img.shape
    if results.multi_hand_landmarks:
        landmark_x = []
        landmark_normalised = []
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms)

        # Mediapipe normalises the landmarks inside of the image
        # To establish them as proper x, y coordinates inside of the image we multiply them by the width
        # and height of the image to use them for further work
        # This is 100% necessary for all further work we do
        for id, lm in enumerate(handLms.landmark):
            px, py = int(lm.x * w), int(lm.y * h)
            landmark_normalised.append([px, py])
            landmark_x.append(px)

        fingers = []
        handtype = results.multi_handedness[0].classification[0].label
        # This is for thumb detection as either out or in relative to the points that build up the thumb
        # Here we basically compare the tip of the thumb to the landmark 2 down (approximately 2 joints down)
        # If the tip of the thumb is further out on the x axis then it is counted as outstretched
        # otherwise it is counted as inside
        if handtype == "Right":
            if landmark_normalised[mediapipe_tip_id[0]][0] > landmark_normalised[mediapipe_tip_id[0] - 1][0]:
                fingers.append(0)
            else:
                fingers.append(1)
        else:
            if landmark_normalised[mediapipe_tip_id[0]][0] < landmark_normalised[mediapipe_tip_id[0] - 1][0]:
                fingers.append(0)
            else:
                fingers.append(1)

        for i in range(1, 5):
            if landmark_normalised[mediapipe_tip_id[i]][1] < landmark_normalised[mediapipe_tip_id[i] - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)


        # Now based on how we detect the fingers we detect different symbols
        # Current limitations include: Currently this is accounting for some level of "average" person
        # if we wanted to make this more inclusive in the future we would have to put work towards that
        # and i encourage that we do if we carry this into our bachelor project
        #
        if 0 not in fingers:
            new_label = "Palm"
            cv2.putText(img, "Detected Palm", (250, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        elif 1 not in fingers:
            new_label = "Fist"
            cv2.putText(img, "Detected Fist", (250, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        elif fingers[1] == 1 and fingers[2] == 1 and not 1 in (fingers[0], fingers[3], fingers[4]):
            new_label = "Peace"
            cv2.putText(img, "Peace!", (250, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        else:
            new_label = None
            cv2.putText(img, "Nothing detected...", (250, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        if new_label is None:
            pass
        elif new_label != label:
            label = new_label
            interface.interface(label)
        # With our normalised coordinates we can figure out our finger points in the x,y coordinate space in the image
        # and use the points for further calculations
        # img = cv2.rectangle(img, (landmark_normalised[5][0] - 5, landmark_normalised[5][1] - 5), (landmark_normalised[5][0] + 5, landmark_normalised[5][1] + 5), (255, 0, 0), 2)
        # Example of how just using the hand landmarks without normalising them first fails
        # img = cv2.rectangle(img, (handLms.landmark[5].x - 5, handLms.landmark[5].y - 5), (handLms.landmark[5].x + 5, handLms.landmark[5].y + 5), (255, 0, 0), 2)


    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



