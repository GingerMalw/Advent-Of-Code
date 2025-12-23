# --- Day 10: Factory ---

from tkinter import filedialog
import ast
from itertools import combinations

def data_split(input_files):
    with open(input_files, "r", encoding='utf-8') as input_data:
        diagrams = []
        for line in input_data.readlines:
            diagram = line.split()
            diagrams.append(diagram)

    return diagrams


def diagram_split(diagram):
    joltage = diagram[-1][1:-1]
    joltage_req = [int(x.strip()) for x in joltage.split(',')]
    del diagram[-1]
    lights = list(str(diagram[0][1:-1]))
    buttons = [
        (b,) if isinstance(b := ast.literal_eval(x), int) else b
        for x in diagram[1:]
    ]
    # print(f'\nLIGHTS: {lights}')
    # print(f'BUTTONS: {buttons}')
    # print(f'JOL_REQ: {joltage_req}')

    buttons_brut_combo = []
    for b in range(1, len(buttons)+1):
        for c in combinations(buttons, b):
            buttons_brut_combo.append(c)
    # print(buttons_brut_combo)
    combo_sorted = sorted(buttons_brut_combo, key=lambda x: (len(x), x))

    return joltage_req, lights, combo_sorted, buttons


def configuration(diagrams):    #PART1
    total = 0
    for diagram in diagrams:
        joltage_req, lights, combo_sorted, buttons = diagram_split(diagram)

        # print(f'\nLIGHTS: {lights}')
        for combo in combo_sorted:
            lights_combo = list("." * len(lights))
            # print(f'COMBO: {combo}')
            # print(f'AMOUNT: {len(combo)}')
            for button in combo:
                for i in button:
                    if lights_combo[i] == ".":
                        lights_combo[i] = "#"
                    elif lights_combo[i] == "#":
                        lights_combo[i] = "."

            print(lights_combo)
            if lights_combo == lights:
                # print(f'COMBO: {combo}')
                # print(f'AMOUNT: {len(combo)}')
                total += int(len(combo))
                break

    return total


def joltage_level(diagrams):    #PART2
    total = 0
    for diagram in diagrams:
        joltage_req, lights, combo_sorted, buttons = diagram_split(diagram)
        print(f'JOL_REQ: {joltage_req}')

        #in progress...
        #maybe starting from joltage and checking the buttons? ...
                    

if __name__ == "__main__":

    input_files = filedialog.askopenfilename()
    diagrams = data_split(input_files)

    print(f"Button presses required for PART1: {configuration(diagrams)}")

    # joltage_level(diagrams)