# --- Day 2: Gift Shop ---

from tkinter import filedialog

def ID_range(input):
    with open(input, "r", encoding='utf-8') as input_file:
        for phrase in input_file:
            IDs_list = phrase.split(",")
            return IDs_list
        

def invalid_search(IDs_list):
    sum = 0
    for element in IDs_list:
        start, end = element.split("-")
        ID_range = list(range(int(start), int(end)+1))

        for number in ID_range:
            length = len(str(number))
            if length % 2 == 0:
                number = str(number)
                half = length // 2
                if int(number[:half]) == int(number[half:]): # compare both parts >> invalid ID requirement
                    sum += int(number)
            else:
                continue

    return sum


def invalid_search_upgrade(IDs_list):
    sum = 0
    for element in IDs_list:
        start, end = element.split('-')
        ID_range = list(range(int(start), int(end)+1))

        for number in ID_range:
            length = len(str(number))
            divided = [mod for mod in range(1, length+1) if length % mod == 0 and mod != length] # checking possible combinations
            divided.sort(reverse=True) # done to start checking from the higher numbers and stop if find (no duplicates)
            for mod in divided:
                number_str = str(number)
                group_from_mod = [int(number_str[i:i+mod]) for i in range(0, length, mod)]
                if len(set(group_from_mod)) == 1:
                    sum += int(number)
                    break
                else:
                    continue

    return sum


if __name__ == "__main__":

    input_files = filedialog.askopenfilename()
    number_list = ID_range(input_files)

    invalid_sum1 = invalid_search(number_list)
    print(f'Sum for invalid IDs PART1: {invalid_sum1}')

    invalid_sum2 = invalid_search_upgrade(number_list)
    print(f'Sum for invalid IDs PART2: {invalid_sum2}')