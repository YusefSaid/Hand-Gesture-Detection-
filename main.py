import cv2
import mediapipe as mp
import time
import deepLearning
import interface

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
# i = 0
label = None
new_label = None
while True:
    # i += 1
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        # if i % 10 == 0:
        image, new_label = deepLearning.deep_learning(img)
        if new_label is None:
            pass
        elif new_label != label:
            label = new_label
            img = image
            interface.interface(label)

        # for handLms in results.multi_hand_landmarks:
        # mpDraw.draw_landmarks(img, handLms)

    # if results.multi_hand_landmarks:
    #    for handLms in results.multi_hand_landmarks:
    #        mpDraw.draw_landmarks(img, imgRGB)

    cv2.imshow("Image", img)
    cv2.waitKey(1)