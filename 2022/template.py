import aocd

date =
data = aocd.get_data(year=2022, day=date).split("\n")  # TODO: change day

for line in data:
    print(line)
