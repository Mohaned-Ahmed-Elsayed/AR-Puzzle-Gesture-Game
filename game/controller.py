# game/controller.py

from config.settings import (
    GRID_SIZE,
    TILE_SIZE,
    BOARD_X,
    BOARD_Y
)


class PuzzleController:

    def __init__(self):

        self.held = None

    def update(self, finger, gesture, puzzle):

        if finger is None:
            return

        pinch = gesture == "pinch"

        fx, fy = finger

        col = (fx - BOARD_X) // TILE_SIZE
        row = (fy - BOARD_Y) // TILE_SIZE

        if not (0 <= col < GRID_SIZE and 0 <= row < GRID_SIZE):
            return

        idx = row * GRID_SIZE + col

        # Hover
        puzzle.hover_idx = idx

        # Pick
        if pinch and self.held is None:

            self.held = idx

        # Drop
        elif not pinch and self.held is not None:

            if idx != self.held:
                puzzle.swap(self.held, idx)

            self.held = None

        puzzle.held_idx = self.held