#!/usr/bin/python3
"""
Module for 0x0C. N Queens.
Holberton School
Specializations - Interview Preparation ― Algorithms
"""
import numpy as np
import itertools
from functools import partial

BLOCKED = 0
FREE = 1
OCCUPIED = 2

class NQueens:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = np.full((board_size, board_size), FREE, dtype=int)
        self.solutions = 0

    def is_valid_coord(self, coordinate):
        row, column = coordinate
        return 0 <= row < self.board_size and 0 <= column < self.board_size

    def block_positions(self, row, column):
        blocked_positions = set()

        # Block left
        for col in range(column - 1, -1, -1):
            blocked_positions.add((row, col))

        # Block right
        for col in range(column + 1, self.board_size):
            blocked_positions.add((row, col))

        # Block up
        for rw in range(row - 1, -1, -1):
            blocked_positions.add((rw, column))

        # Block down
        for rw in range(row + 1, self.board_size):
            blocked_positions.add((rw, column))

        # Block L up-diag
        rw, col = row, column
        while self.is_valid_coord((rw - 1, col - 1)):
            rw -= 1
            col -= 1
            blocked_positions.add((rw, col))

        # Block L down-diag
        rw, col = row, column
        while self.is_valid_coord((rw + 1, col - 1)):
            rw += 1
            col -= 1
            blocked_positions.add((rw, col))

        # Block R up-diag
        rw, col = row, column
        while self.is_valid_coord((rw - 1, col + 1)):
            rw -= 1
            col += 1
            blocked_positions.add((rw, col))

        # Block R down-diag
        rw, col = row, column
        while self.is_valid_coord((rw + 1, col + 1)):
            rw += 1
            col += 1
            blocked_positions.add((rw, col))

        return blocked_positions

    def place_queens(self, row=0):
        if row == self.board_size:
            self.solutions += 1
            print(self.board)
            print()
            return

        for col in range(self.board_size):
            if self.board[row, col] == FREE and row not in self.block_positions(row, col):
                self.board[row, col] = OCCUPIED
                self.place_queens(row + 1)
                self.board[row, col] = FREE

if __name__ == "__main__":
    board_size = 5
    n_queens = NQueens(board_size)
    n_queens.place_queens()
    print(f"{n_queens.solutions} solutions")
    print("Finished")
    