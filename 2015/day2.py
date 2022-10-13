# Part 1

with open('day2_volume.txt') as f:
    total = 0
    for line in f:

        l, w, h = map(int, line.split('x'))
        wrap = 2 * (l * w) + (w * h) + (h * l)
        extra = min(l * w, w * h, h * l)
        paper = wrap + extra
        total += paper

        print(f"Total {total}")
