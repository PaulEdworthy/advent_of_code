# Part 1

with open('text_input/day_1.txt') as f:
    current_total = 0
    totals = []

    lines = f.readlines()
    for line in lines:
        if line == '\n':
            totals.append(current_total)
            current_total = 0

        else:
            line = int(line)
            current_total += line

    totals.sort(reverse=True)
    print(totals[0])

# Part 2

print(totals[0] + totals[1] + totals[2])
