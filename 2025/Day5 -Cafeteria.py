# --- Day 5: Cafeteria ---

from tkinter import filedialog
import re

def split(data_input):
    with open(data_input, "r", encoding='utf-8') as input:
        fresh_range = []
        food_id = []
        for line in input.readlines():
            if line.strip():
                if re.match(r".*-.*", line):
                    fresh_range.append(line.strip())
                else:
                    food_id.append(line.strip())

    return fresh_range, food_id


def compare(fresh, food):
    etable = []
    for id in food:
        for line in fresh:
            start, end = line.split("-")
            if int(id) >= int(start) and int(id) <= int(end):
                etable.append(id)
                break
    
    etable = set(etable)
    return len(etable)


def freshings(fresh):
    # math: 2 ranges: [a, b] and [c, d]
    # overalping if: a ≤ d and c ≤ b
    
    ranges = []
    for f in fresh:
        start, end = map(int, f.split("-"))
        ranges.append((start, end))

    ranges.sort()
    merged = []
    for start, end in ranges:
        if not merged:
            merged.append([start, end])
            continue

        last_start, last_end = merged[-1]
        if start <= last_end and last_start <= end:
            # end ≥ last_start always true due to sort
            merged[-1][1] = max(last_end, end)
            # changing only end
        else:
            merged.append([start, end])

    fresh = [f"{a}-{b}" for a, b in merged]
    
    fresh_stack = 0
    for line in fresh:
        start, end = line.split("-")
        x = int(end) - int(start) + 1
        fresh_stack += x

    return fresh_stack


if __name__ == "__main__":

    input_files = filedialog.askopenfilename()
    fresh, food = split(input_files)
    print(f"Total amount of fresh food for PART1: {compare(fresh, food)}")
    print(f"Total amount of fresh food for PART2: {freshings(fresh)}")