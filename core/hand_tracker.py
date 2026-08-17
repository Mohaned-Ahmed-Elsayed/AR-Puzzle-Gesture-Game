import cv2
import mediapipe as mp
import math

mp_hands = mp.solutions.hands


class HandTracker:

    def __init__(self):

        self.hands = mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.mp_draw = mp.solutions.drawing_utils

    # =========================================
    # DISTANCE FUNCTION
    # =========================================
    def dist(self, a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

    # =========================================
    # MAIN PROCESS
    # =========================================
    def process(self, frame):

      h, w, _ = frame.shape

      rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      result = self.hands.process(rgb)

      finger = None
      gesture = "none"

      if result.multi_hand_landmarks:

          hand = result.multi_hand_landmarks[0]
          lm = hand.landmark

          # =========================
          # KEY POINTS
          # =========================
          ix, iy = int(lm[8].x * w), int(lm[8].y * h)   # index
          tx, ty = int(lm[4].x * w), int(lm[4].y * h)   # thumb

          finger = (ix, iy)

          # =========================
          # NORMALIZED PINCH (SCALE-INVARIANT)
          # =========================
          pinch_distance = self.dist((ix, iy), (tx, ty))

          wx, wy = lm[0].x * w, lm[0].y * h   # wrist
          mx, my = lm[9].x * w, lm[9].y * h   # middle finger MCP

          hand_size = self.dist((wx, wy), (mx, my))

          pinch_ratio = pinch_distance / hand_size if hand_size > 0 else 1

          if pinch_ratio < 0.35:
              gesture = "pinch"

          # =========================
          # OPEN HAND (RESET)
          # =========================
          elif (
              lm[8].y < lm[6].y and
              lm[12].y < lm[10].y and
              lm[16].y < lm[14].y and
              lm[20].y < lm[18].y
          ):
              gesture = "open"

          else:
              gesture = "none"

          # =========================
          # DRAW HAND
          # =========================
          self.mp_draw.draw_landmarks(
              frame,
              hand,
              mp_hands.HAND_CONNECTIONS
          )

      return finger, gesture