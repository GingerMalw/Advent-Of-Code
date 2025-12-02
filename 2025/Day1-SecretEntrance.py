# --- Day 1: Secret Entrance ---

from tkinter import filedialog

def creating_numbers(x,y,z):
    numbers = list(range(x,y+1))
    start_point = numbers.index(z)

    return numbers, start_point


def decoding_sequence(numbers, start, input_files):
    position = start
    password = 0

    with open(input_files, "r", encoding='utf-8') as sequence:
        for rotation in sequence:
            rotation = rotation.strip()
            direction = str(rotation[0])
            step = int(rotation[1:])

            if direction == "R":
                position = (position + step) % len(numbers)
            else: # direction for "L"
                position = (position - step) % len(numbers)
            if position == 0:
                password += 1

    return password


def decoding_sequence_0x434C49434B(numbers, start, input_files):
    position = start
    password = 0

    with open(input_files, "r", encoding='utf-8') as sequence:
        for rotation in sequence:
            rotation = rotation.strip()
            direction = str(rotation[0])
            step = int(rotation[1:])

            if direction == "R":
                password += (position + step) // len(numbers) #amount of clicks
                position = (position + step) % len(numbers)
            else: # direction for "L"
                rewerse = (len(numbers) - position) % len(numbers) # designed to run as "R"
                password += (rewerse + step) // len(numbers) #amount of clicks
                position = (position - step) % len(numbers)

    return password


if __name__ == "__main__":

    input_files = filedialog.askopenfilename()
    numbers, start_point = creating_numbers(0,99,50)

    password_1 = decoding_sequence(numbers, start_point, input_files)
    print(f"The password for PART1: {password_1}")
    
    password_2 = decoding_sequence_0x434C49434B(numbers, start_point, input_files)
    print(f"The password for PART2: {password_2}")