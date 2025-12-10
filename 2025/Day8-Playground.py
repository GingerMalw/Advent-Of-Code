# --- Day 8: Playground ---

from tkinter import filedialog
from math import sqrt

def dist_pairs(input_files):
    with open(input_files, "r", encoding='utf-8') as input:
        boxes = []
        for line in input.readlines():
            x,y,z = map(int, line.split(','))
            boxes.append((x,y,z))

    dist_pairs = []

    for a in range(len(boxes)):
        for b in range(a+1, len(boxes)):
            point1 = boxes[a]
            point2 = boxes[b]

            dx = point2[0] - point1[0]
            dy = point2[1] - point1[1]
            dz = point2[2] - point1[2]

            distance = sqrt(dx*dx + dy*dy + dz*dz)
            dist_pairs.append({'distance': distance, 'points': (point1, point2)})

    dist_pairs.sort(key=lambda pair:pair['distance'])
    return dist_pairs


def circuts(dist_pairs):
    x = input(f"Enter amount of shortest connections to check: ")
    connections = [pair['points'] for pair in dist_pairs[:int(x)]]
    sizes = []

    while connections:
        circut = []
        
        change = True
        while change:
            change = False
            to_remove = []
            for i, jun in enumerate(connections):
                if not circut:
                    circut.extend(jun)
                    to_remove.append(i)

                elif jun[0] in circut and jun[1] in circut:
                    to_remove.append(i)

                elif jun[0] in circut or jun[1] in circut:
                    circut.extend(jun)
                    to_remove.append(i)

                if to_remove:
                    change = True

            for ind in sorted(set(to_remove), reverse=True):
                del connections[ind]

        sizes.append(len(set(circut)))

    sizes.sort(reverse=True)
    multiplication = sizes[0] * sizes[1] * sizes[2]
    
    return multiplication

                
def ext_cables(dist_pairs):
    connections = [pair['points'] for pair in dist_pairs]
    unique_points = {p for pair in connections for p in pair}

    circuts = []
    result = 0

    for p1, p2 in connections:
        circut_1 = None
        circut_2 = None

        for c in circuts:
            if p1 in c:
                circut_1 = c
            if p2 in c:
                circut_2 = c

        if circut_1 is None and circut_2 is None:
            circuts.append({p1,p2})

        elif circut_1 is not None and circut_2 is None:
            circut_1.add(p2)
            
        elif circut_1 is None and circut_2 is not None:
            circut_2.add(p1)

        elif circut_1 is not circut_2:
            # both already connected but in different circuts
            circut_1.update(circut_2)
            circuts.remove(circut_2)

        if len(circuts) == 1 and len(circuts[0]) == len(unique_points):
            result = p1[0] * p2[0]
            break

    return int(result)


if __name__ == "__main__":

    input_files = filedialog.askopenfilename()
    pairs = dist_pairs(input_files)
    print(f"Multiplication for 3 largest circuts for PART1: {circuts(pairs)}")

    end = ext_cables(pairs)
    print(f"X coordinates multiplication for last two junction boxes for PART2: {end}")