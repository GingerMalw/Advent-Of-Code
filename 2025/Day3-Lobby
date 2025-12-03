# --- Day 3: Lobby ---

from tkinter import filedialog

def joltage(input_files):
    with open(input_files, "r", encoding='utf-8') as input:
        total_joltage = 0
        for line in input.readlines():
            bank = line.strip()
            battery_one = max(bank[0:-1])
            battery_one_pos = bank.index(battery_one)
            battery_two = max(bank[battery_one_pos + 1:])
            joltage = battery_one + battery_two
            total_joltage += int(joltage)

        return total_joltage
    

def larger_joltage(input_files):
    with open(input_files, "r", encoding='utf-8') as input:
        total_joltage = 0
        for line in input.readlines():
            bank = line.strip()
            amount = len(bank)
            start = 0
            sequence = 12
            batteries = []
            
            while sequence != 0:
                window = bank[start:((amount+1)-sequence)]
                battery = max(window)
                battery_pos = start + window.index(battery)
                start = battery_pos + 1
                sequence -= 1
                batteries.append(battery)
            
            battery_joltage = int(''.join(str(bat) for bat in batteries))
            total_joltage += battery_joltage

        return total_joltage  


if __name__ == "__main__":

    input_files = filedialog.askopenfilename()
    
    joltage_1 = joltage(input_files)
    print(f'Total output joltage for PART1: {joltage_1}')
    joltage_2 = larger_joltage(input_files)
    print(f'Total output joltage for PART2: {joltage_2}')