# Part 1

with open('day2_volume.txt') as f:
    total = 0
    total_extra = 0
    for line in f:

        l, w, h = sorted(map(int, line.split('x')))
        wrap = (2 * l * w) + (2 * w * h) + (2 * h * l)
        extra = (l * w)
        paper = wrap + extra
        total += paper

        print(f"Total {total}")

# Part 2
        bow = l * w * h
        ribbon = 2 * (l + w)
        total_extra += (bow + ribbon)

        print(f"Ribbon {total_extra}")
