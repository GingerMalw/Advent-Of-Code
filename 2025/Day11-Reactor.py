# --- Day 11: Reactor ---

from tkinter import filedialog

def data_split(input_files):    #for PART1
    with open(input_files, "r", encoding='utf-8') as input_data:
        devices = []
        for line in input_data.readlines():
            device = line.split()
            devices.append(device)

    return devices


def paths(devices):     #for PART1
    connections = []
    path_amount = 0

    for con in devices:
        if con[0] == "you":
            for el in con[1:]:
                connections.append(el + ":")
    print(f"Connections: {connections}")

    for el in connections:
        for con in devices:
            if con[0] == el:
                if con[1] == "out":
                    path_amount += 1
                else:
                    for el in con[1:]:
                        connections.append(el + ":")

    print(f"Connections: {connections}")

    return path_amount


def data_dictionary(input_files):   #for PART2
    with open(input_files, "r", encoding='utf-8') as input_data:
        devices = {}
        for line in input_data.readlines():
            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                values = [v.strip() for v in values.split()]
                devices[key] = value

    return devices


def paths2(devices_dict):   #for PART2
    all_paths = []
    path_amount = 0
    # from 'svr' to 'out' and must contain both 'dac' and 'fft' ...
    # in progress ....

    start = devices['svr']
    print(f"START: {start}")


if __name__ == "__main__":

    input_files = filedialog.askopenfilename()
    devices = data_split(input_files)

    print(f"Amount of different paths for PART1: {paths(devices)}")

    input_files2 = filedialog.askopenfilename()
    devices2 = data_dictionary(input_files2)
    paths(devices2)

    # print(f"Amount of different paths for PART2: {paths2(devices2)}")
