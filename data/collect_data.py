# collect_data.py
import cv2
import csv
import mediapipe as mp


mp_hands = mp.solutions.hands

hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)

label = input("Enter gesture label: ")

with open("dataset.csv", "a", newline="") as file:

    writer = csv.writer(file)

    while True:

        ret, frame = cap.read()

        frame = cv2.flip(frame, 1)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = hands.process(rgb)

        if result.multi_hand_landmarks:

            hand = result.multi_hand_landmarks[0]

            row = []

            for lm in hand.landmark:
                row.append(lm.x)
                row.append(lm.y)

            row.append(label)

            writer.writerow(row)

        cv2.imshow("Collect Data", frame)

        key = cv2.waitKey(1)

        if key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()