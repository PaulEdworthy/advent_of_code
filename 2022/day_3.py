import aocd

date = 3
data = aocd.get_data(year=2022, day=date).split("\n")


def convert(char):
    if char.islower():
        return ord(char) - 96
    elif char.isupper():
        return ord(char) - 38


def part_1(data):
    total = 0
    for line in data:
        nums = []

        for char in line:
            temp = convert(char)
            nums.append(temp)

        b = nums[:len(nums) // 2]
        c = nums[len(nums) // 2:]
        dupl = set(b).intersection(c)
        for i in dupl:
            total += i

        # print(total)


def part_2(data):
    start = 0
    end = len(data)
    step = 3
    total = 0

    for i in range(start, end, step):
        n = i
        split = ((data[n:n + step]))
        common = set(split[0]).intersection(split[1]).intersection(split[2])
        for i in common:
            asc = convert(i)
            total += asc
    print(total)


part_1(data)
part_2(data)
