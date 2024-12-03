import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from load_aoc_data import get_aoc_input

data = get_aoc_input(2024, 2)

# test the input just grabbing the first and last lines
print(f"First line {data[0]}, and the last line {data[-1]}")
