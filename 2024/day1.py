import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from load_aoc_data import get_aoc_input

data = get_aoc_input(2024, 1)

left, right = [], []
total = 0

for line in data:
    value = line.split()
    left.append(int(value[0]))
    right.append(int(value[1]))

left.sort()
right.sort()

# Part 1
for i in range(len(left)):
    total += abs(left[i] - right[i])

# Part 2
for i in left:
    total += i * right.count(i)

print(total)