# game/renderer.py

import cv2

from config.settings import (
    GRID_SIZE,
    TILE_SIZE,
    BOARD_X,
    BOARD_Y
)


class Renderer:

    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    YELLOW = (0, 255, 255)
    DARK = (30, 30, 30)

    def draw_puzzle(self, frame, puzzle):

        board_size = GRID_SIZE * TILE_SIZE

        cv2.rectangle(
            frame,
            (BOARD_X - 10, BOARD_Y - 10),
            (
                BOARD_X + board_size + 10,
                BOARD_Y + board_size + 10
            ),
            self.DARK,
            -1
        )

        cv2.putText(
            frame,
            "PUZZLE",
            (BOARD_X, BOARD_Y - 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            self.GREEN,
            3
        )

        for row in range(GRID_SIZE):

            for col in range(GRID_SIZE):

                idx = row * GRID_SIZE + col

                tile_index = puzzle.board_state[idx]

                tile = puzzle.tiles[tile_index]

                px = BOARD_X + col * TILE_SIZE
                py = BOARD_Y + row * TILE_SIZE

                frame[
                    py:py + TILE_SIZE,
                    px:px + TILE_SIZE
                ] = tile

                cv2.rectangle(
                    frame,
                    (px, py),
                    (px + TILE_SIZE, py + TILE_SIZE),
                    self.WHITE,
                    2
                )

        # Hover
        if puzzle.hover_idx is not None:

            col = puzzle.hover_idx % GRID_SIZE
            row = puzzle.hover_idx // GRID_SIZE

            hx = BOARD_X + col * TILE_SIZE
            hy = BOARD_Y + row * TILE_SIZE

            cv2.rectangle(
                frame,
                (hx, hy),
                (hx + TILE_SIZE, hy + TILE_SIZE),
                self.YELLOW,
                4
            )

        # Selected
        if puzzle.held_idx is not None:

            col = puzzle.held_idx % GRID_SIZE
            row = puzzle.held_idx // GRID_SIZE

            sx = BOARD_X + col * TILE_SIZE
            sy = BOARD_Y + row * TILE_SIZE

            cv2.rectangle(
                frame,
                (sx, sy),
                (sx + TILE_SIZE, sy + TILE_SIZE),
                self.GREEN,
                6
            )

            cv2.putText(
                frame,
                "SELECTED",
                (sx + 5, sy - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                self.GREEN,
                2
            )