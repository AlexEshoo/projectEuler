import numpy as np
import random

class Board(object):
    rows = 9
    cols = 9

    def __init__(self, grid):
        self.possible_values = np.zeros([9, 9, 9], dtype=int).tolist()
        for i in range(9):
            for j in range(9):
                self.possible_values[i][j] = set(range(1, 10))

        self.solution = grid

        for i in range(Board.rows):
            for j in range(Board.cols):
                n = self.solution[i,j]
                if n:
                    self.put_value(n, i, j)

    def solve(self):
        while self.step():
            pass

        if not 0 in self.solution:
            return  # puzzle fully solved.

        for i in range(Board.rows):
            for j in range(Board.cols):
                new_board = Board(self.solution)

                if new_board.possible_values[i][j]:
                    val = random.sample(new_board.possible_values[i][j], 1)[0]
                    new_board.possible_values[i][j].remove(val)
                    new_board.put_value(val, i, j)

                    new_board.solve()

                    if not 0 in new_board.solution:
                        self.possible_values = new_board.possible_values
                        self.solution = new_board.solution
                        return # puzzle solved


    def step(self):
        for i in range(Board.rows):
            for j in range(Board.cols):
                if len(self.possible_values[i][j]) == 1:
                    self.put_value(self.possible_values[i][j].pop(), i, j)
                    return True

        return False

    def put_value(self, n, row, col):
        self.solution[row, col] = n
        self.possible_values[row][col] = {n}

        # Remove possible values in same column
        for i in range(Board.rows):
            self.possible_values[i][col].discard(n)

        # Remove possible values from same row
        for j in range(Board.cols):
            self.possible_values[row][j].discard(n)

        # Remove possible values from same nonet
        for index in self.nonet(row, col):
            self.possible_values[index[0]][index[1]].discard(n)

    @staticmethod
    def nonet(row, col):
        origin = ((row // 3) * 3, (col // 3) * 3)

        nonet_list = []
        for i in range(3):
            for j in range(3):
                nonet_list.append((origin[0] + i, origin[1] + j))

        return nonet_list

    @property
    def solution_number(self):
        return int("".join([str(self.solution[0,i]) for i in range(3)]))

if __name__ == '__main__':
    with open("resources/p096_sudoku.txt") as f:
        f.readline()  # skip first line
        grid_strings = [""] * 50
        i = 0
        for line in f:
            if line[0] != 'G':
                grid_strings[i] += line
            else:
                i += 1

    grids = []
    for g in grid_strings:
        gg = []
        for row in g.strip().split('\n'):
            gg.append(list(row))

        grids.append(np.array(gg, dtype=int))

    answer = 0
    for g in grids:
        b = Board(g)
        b.solve()
        if '0' in str(b.solution_number):
            print("SOLUTION NUMBER CONTAINED 0")

        answer += b.solution_number
        print(b.solution)

    print(answer)