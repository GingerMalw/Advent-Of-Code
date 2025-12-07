# --- Day 6: Trash Compactor ---

from tkinter import filedialog
import math

def grid(data_input):
    with open(data_input, "r", encoding='utf-8') as input:
        elements = input.read().split()
        # print(elements)
    
    n = sum(1 for x in elements if x in ["*", "+"])
    grid = [elements[i:i+n] for i in range(0,len(elements), n)]

    return grid


def math_solution(grid):
    problems = list(zip(*grid))
    # print(f"PROBLEMS: {problems}")
    grand_total = 0
    for n in range(0,len(grid[0])):
        problem = list(problems[n])
        # print(f"N: {n}, PROBLEM: {problem}")
        
        if problem[-1] == '*':
            # print("***")
            problem_sum = math.prod(int(x) for x in problem if x.isdigit())
            # print(problem_sum)
            grand_total += problem_sum

        if problem[-1] == '+':
            # print("+++")
            problem_sum = sum(int(x) for x in problem if x.isdigit())
            # print(problem_sum)
            grand_total += problem_sum

    # print(f"TOTAL: {grand_total}")
    return grand_total


def math_cephalopods(data_input):
    pass
    # part 2 to be done later ..........


if __name__ == "__main__":

    input_files = filedialog.askopenfilename()
    input = grid(input_files)
    
    print(f"Grand total for PART1: {math_solution(input)}")
    # print(f"Grand total for PART2: {math_cephalopods(input_files)}")
    # part 2 to be done later ..........