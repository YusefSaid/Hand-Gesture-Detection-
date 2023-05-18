import glob

import cv2
import mediapipe as mp
import time
import os
import math

mpHands = mp.solutions.hands
hands = mpHands.Hands()
# NEW ELEMENT
crop_buffer = 5

def LabelToDataset(label):
    '''
    Takes in label and starts placing pictures into associated folder
    :param label: String
    :return:
    '''
    path = f'\dataset\{label}\image'
    rightPath = r'' + path

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    path = f'{os.getcwd()}/cropped/{label}'
    uncropped_path = f'{os.getcwd()}/uncropped/{label}'

    img_counter = 0
    uncropped_img_counter = 0

    if not os.path.exists(f'cropped'):
        os.mkdir(f'cropped')
    if not os.path.exists(f'uncropped'):
        os.mkdir(f'uncropped')

    if not os.path.exists(f'cropped/{label}'):
        os.mkdir(f'cropped/{label}')
    else:
        img_counter = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

    if not os.path.exists(f'uncropped/{label}'):
        os.mkdir(f'uncropped/{label}')
    else:
        uncropped_img_counter = len([f for f in os.listdir(uncropped_path) if os.path.isfile(os.path.join(uncropped_path, f))])


    while True:

        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break

        cv2.imshow("test", cv2.flip(frame,1))

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
              break
        elif k % 256 == 32:
            # SPACE pressed
            img_name = f"cropped/{label}/{label}_{img_counter}.png"
            uncropped_name = f"uncropped/{label}/{label}_{uncropped_img_counter}.png"
            frameToGrab = cv2.flip(frame, 1)
            imgRGB = cv2.cvtColor(frameToGrab, cv2.COLOR_BGR2RGB)
            cv2.imwrite(uncropped_name, imgRGB)
            results = hands.process(imgRGB)
            xmin = 1.0
            ymin = 1.0
            xmax = -1.0
            ymax = -1.0
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    for landmark in hand_landmarks.landmark:
                        xmin = min(xmin, landmark.x)
                        ymin = min(ymin, landmark.y)
                        xmax = max(xmax, landmark.x)
                        ymax = max(ymax, landmark.y)
            print("{} written!".format(img_name))

            #xmin = int(xmin * frame.shape[1])
            #xmax = int(xmax * frame.shape[1])
            #ymin = int(ymin * frame.shape[0])
            #ymax = int(ymax * frame.shape[0])
            pxmin = min(math.floor((xmin * frame.shape[1])-crop_buffer), frame.shape[1] - 1)
            pxmax = min((math.floor(xmax * frame.shape[1])+crop_buffer), frame.shape[1] - 1)
            pymin = min((math.floor(ymin * frame.shape[0])-crop_buffer), frame.shape[0] - 1)
            pymax = min((math.floor(ymax * frame.shape[0])+crop_buffer), frame.shape[0] - 1)
            # CHANGED VALUES
            cropped_frame = imgRGB[pymin:pymax,pxmin:pxmax]

            if cropped_frame.size != 0:
                cv2.imwrite(img_name, cropped_frame)
                img_counter += 1
            uncropped_img_counter += 1



    cam.release()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    LabelToDataset(input("Enter label for data: "))