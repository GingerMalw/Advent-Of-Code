# --- Day 9: Movie Theater ---

from tkinter import filedialog
from math import sqrt
# import shapely
# from shapely.geometry import Point, Polygon


def pairs(input_files):
    with open(input_files, "r", encoding='utf-8') as input:
        red_tiles = []
        for line in input.readlines():
            x,y = map(int, line.split(','))
            red_tiles.append((x,y))

    return red_tiles


def largest_rec(red_tiles):
    tiles_area = []

    for a in range(len(red_tiles)):
        for b in range(a+1, len(red_tiles)):
            t1 = red_tiles[a]
            t2 = red_tiles[b]

            dx = abs(t2[0] - t1[0]) +1
            dy = abs(t2[1] - t1[1]) +1
            area = dx*dy
            tiles_area.append({'area': area, 'points': (t1, t2)})

    tiles_area.sort(key=lambda pair:pair['area'], reverse=True)
    best = tiles_area[0]

    return best


def allowed(red_tiles):
    pass


def pairs_limitation(red_tiles):
    pass


def largest_rec_upgrade():
    pass



if __name__ == "__main__":

    input_files = filedialog.askopenfilename()
    red_tiles = pairs(input_files)
    print(f"Largest rectangle for PART1: {largest_rec(red_tiles)}")

    # PART2 in progress ........