# --- Day 4: Printing Department ---

from tkinter import filedialog
import re

def grid(data_input):
    with open(data_input, "r", encoding='utf-8') as input:
        grid = []
        for line in input.readlines():
            grid.append(line.strip())

    return grid


def papper_roll(grid):
    rolls = 0
    for y, row in enumerate(grid):
        for x, place in enumerate(row):
            if re.match(r"@", place):
                move = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
                adjacent = [grid[y+dy][x+dx] for dy,dx in move if y+dy in range(0,len(grid)) and x+dx in range(0,len(row))]
                if sum(1 for a in adjacent if a == "@") < 4:
                    rolls += 1

    return rolls


def papper_roll_pro(grid):
    rolls = 0
    while True:
        removed = []
        for y, row in enumerate(grid):
            for x, place in enumerate(row):
                if re.match(r"@", place):
                    move = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
                    adjacent = [grid[y+dy][x+dx] for dy,dx in move if y+dy in range(0,len(grid)) and x+dx in range(0,len(row))]
                    if sum(1 for a in adjacent if a == "@") < 4:
                        rolls += 1
                        removed.append((y,x))

        if not removed:
            break
        else:
            for y,x in removed:
                row_list = list(grid[y])
                row_list[x] = "x"
                grid[y] = ''.join(row_list)

    return rolls


if __name__ == "__main__":

    input_files = filedialog.askopenfilename()
    input = grid(input_files)
    print(f"Rolls of paper in total for PART1: {papper_roll(input)}")
    print(f"Rolls of paper in total for PART2: {papper_roll_pro(input)}")