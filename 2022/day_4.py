import aocd

date = 4
data = aocd.get_data(year=2022, day=date).split("\n")

total = overlap = 0

for line in data:
    line = line.strip()
    a, b = line.split(',')

    al, ah = a.split('-')
    al = int(al)
    ah = int(ah)
    bl, bh = b.split('-')
    bl = int(bl)
    bh = int(bh)
    if (al <= bl and ah >= bh) or (al >= bl and ah <= bh):
        total += 1
    if bl <= al <= bh or bl <= ah <= bh or al <= bl <= ah and al <= bh <= ah:
        overlap += 1
print(overlap)
