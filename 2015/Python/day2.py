# Part 1

with open('text_input/day2_volume.txt') as f:
    total = 0
    total_extra = 0
    for line in f:

        l, w, h = sorted(map(int, line.split('x')))
        # sorting here just allows you to use l x w instead
        # of finding the min in the extra variable

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
