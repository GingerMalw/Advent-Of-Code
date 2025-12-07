# --- Day 7: Laboratories ---

# IN PROGRESS!!

from tkinter import filedialog
import re

def grid(data_input): # return grid
    with open(data_input, "r", encoding='utf-8') as input:
        grid = []
        for line in input.readlines():
            grid.append(line.strip())

    return grid


def manifold(input):
    # split = 0
    for y, row in enumerate(input):
        start_x = row.find('S')
        if start_x != -1:
            start = [y, start_x]
            print(start)

    for row_id in range(start[0]+1, len(input)):
        print(row_id, input[row_id]) 

        # IN PROGRESS!!


if __name__ == "__main__":

    input_files = filedialog.askopenfilename()
    input = grid(input_files)
    print(input)

    # print(f"Amount of split for PART1: {manifold(input)}")