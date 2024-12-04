import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from load_aoc_data import get_aoc_input

data = get_aoc_input(2024, 2)

safe = 0

def is_increasing(input):
    return all(input[i] < input[i + 1] and input[i + 1] - input[i] <= 3 for i in range(len(input) - 1))


def is_decreasing(input):
    return all(input[i] > input[i + 1] and input[i] - input[i + 1] <= 3 for i in range(len(input) - 1))


for line in data:
    value = [int(i) for i in line.split()] # convert a list of strings to a list of ints
    
    if is_increasing(value) or is_decreasing(value):
        safe += 1


print(safe)
