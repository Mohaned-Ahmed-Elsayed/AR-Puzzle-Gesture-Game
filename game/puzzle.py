# game/puzzle.py

import cv2
import random

from config.settings import (
    GRID_SIZE,
    TILE_SIZE
)


class Puzzle:

    def __init__(self):

        self.tiles = []

        self.correct_order = []

        self.board_state = []

        self.hover_idx = None
        self.held_idx = None

    def create(self, roi):

        roi = cv2.resize(
            roi,
            (
                GRID_SIZE * TILE_SIZE,
                GRID_SIZE * TILE_SIZE
            )
        )

        self.tiles = []

        for row in range(GRID_SIZE):

            for col in range(GRID_SIZE):

                tile = roi[
                    row * TILE_SIZE:(row + 1) * TILE_SIZE,
                    col * TILE_SIZE:(col + 1) * TILE_SIZE
                ]

                self.tiles.append(tile)

        self.correct_order = list(range(9))

        self.board_state = self.correct_order.copy()

        while True:

            random.shuffle(self.board_state)

            if self.board_state != self.correct_order:
                break

    def swap(self, idx1, idx2):

        self.board_state[idx1], self.board_state[idx2] = (
            self.board_state[idx2],
            self.board_state[idx1]
        )

    def is_solved(self):

        return self.board_state == self.correct_order