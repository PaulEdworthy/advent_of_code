import sys
import os
import re
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from load_aoc_data import get_aoc_input

input = get_aoc_input(2024, 3)
data = ''.join(input)

total = 0

matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
for i in matches:
    total += int(i[0]) * int(i[1])
print(total)
