import warnings
warnings.filterwarnings("ignore")

import cv2

from core.camera import Camera
from core.hand_tracker import HandTracker

from game.puzzle import Puzzle
from game.renderer import Renderer
from game.controller import PuzzleController


# =====================================================
# INIT
# =====================================================

camera = Camera()
tracker = HandTracker()

puzzle = Puzzle()
renderer = Renderer()
controller = PuzzleController()

roi_ready = False

selecting = False
x1 = y1 = x2 = y2 = 0

release_frames = 0
RELEASE_THRESHOLD = 6

reset_counter = 0
RESET_THRESHOLD = 20


# =====================================================
# MAIN LOOP
# =====================================================

while True:

    frame = camera.read()
    if frame is None:
        break

    h, w, _ = frame.shape

    # =================================================
    # HAND TRACKING
    # =================================================

    finger, gesture = tracker.process(frame)


    # =========================
    # GESTURE UI (PUT HERE)
    # =========================

    cv2.rectangle(frame, (20, 90), (300, 170), (30, 30, 30), -1)
    cv2.rectangle(frame, (20, 90), (300, 170), (255, 255, 255), 2)

    if gesture == "pinch":
     g_color = (0, 255, 0)
    elif gesture == "open":
     g_color = (255, 0, 255)
    else:
     g_color = (0, 255, 255)

    cv2.putText(frame, "Gesture", (30, 120),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7,
            (200, 200, 200), 2)

    cv2.putText(frame, gesture.upper(), (30, 155),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            g_color, 3)

    cv2.circle(frame, (280, 130), 12, g_color, -1)

    pinch = (gesture == "pinch")
    open_hand = (gesture == "open")

    # =================================================
    # CURSOR
    # =================================================

    if finger:
        cv2.circle(frame, finger, 10, (255, 120, 0), -1)

        if pinch:
            cv2.circle(frame, finger, 18, (0, 255, 0), 3)

    # =================================================
    # ROI SELECTION (FIXED LOGIC)
    # =================================================

    if not roi_ready:

        cv2.putText(frame,
                    "PINCH and DRAG to select image",
                    (30, h - 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 0),
                    2)

        cv2.putText(frame,
                    "Release fingers to confirm",
                    (30, h - 25),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 0),
                    2)

        if finger:

            # START SELECTION
            if pinch and not selecting:

                selecting = True
                release_frames = 0
                x1, y1 = finger
                x2, y2 = finger

            # UPDATE SELECTION
            if selecting and pinch:

                x2, y2 = finger

            # DRAW BOX
            if selecting:

                cv2.rectangle(frame,
                              (x1, y1),
                              (x2, y2),
                              (0, 255, 0),
                              3)

            # RELEASE DETECTION (FIXED)
            if selecting and not pinch:
                release_frames += 1
            else:
                release_frames = 0

            # CONFIRM ROI
            if selecting and release_frames > RELEASE_THRESHOLD:

                selecting = False

                xa, xb = sorted([x1, x2])
                ya, yb = sorted([y1, y2])

                roi = frame[ya:yb, xa:xb]

                if roi.size > 0 and roi.shape[0] > 100 and roi.shape[1] > 100:

                    puzzle.create(roi)
                    roi_ready = True

    # =================================================
    # GAME
    # =================================================

    if roi_ready:

        renderer.draw_puzzle(frame, puzzle)

        controller.update(finger, gesture, puzzle)

        # RESET
        if open_hand:

            reset_counter += 1

            cv2.putText(frame,
                        "OPEN HAND TO RESET...",
                        (350, 650),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (255, 0, 255),
                        3)

            bar = int((reset_counter / RESET_THRESHOLD) * 300)

            cv2.rectangle(frame,
                          (350, 680),
                          (350 + bar, 710),
                          (255, 0, 255),
                          -1)

            cv2.rectangle(frame,
                          (350, 680),
                          (650, 710),
                          (255, 255, 255),
                          2)

            if reset_counter > RESET_THRESHOLD:

                puzzle = Puzzle()
                controller = PuzzleController()
                roi_ready = False
                selecting = False
                reset_counter = 0

        else:
            reset_counter = 0

        # WIN CONDITION
        if puzzle.is_solved():

            overlay = frame.copy()
            cv2.rectangle(overlay, (0, 0), (w, h), (0, 255, 0), -1)

            frame = cv2.addWeighted(overlay, 0.25, frame, 0.75, 0)

            cv2.putText(frame,
                        "YOU WIN!",
                        (430, 100),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        2,
                        (255, 255, 255),
                        5)

    # =================================================
    # SHOW
    # =================================================

    cv2.imshow("AR Puzzle Game", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# =====================================================
# CLEANUP
# =====================================================

camera.release()
cv2.destroyAllWindows()