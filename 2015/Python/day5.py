# Part 1

vowels = 'aeiou'
nice_count = 0


def check_vowels(line):
    count = 0
    for c in line:
        if c in vowels:
            count += 1
    if count >= 3:
        return True


def check_duplicate(line):
    count = 0
    for c in line:
        if c + c in line:
            count += 1
    if count > 0:
        return True


def check_omitted(line):
    for pair in ["ab", "cd", "pq", "xy"]:
        if pair in line:
            return False
    return True


with open("text_input/day5_naughty_or_nice.txt") as f:
    for i in f.readlines():
        if check_vowels(i):
            if check_duplicate(i):
                if check_omitted(i):
                    nice_count += 1
    # print(nice_count)

f.close()

# Part 2

nice_count = 0


def check_triple(line):
    for i in range(len(line) - 2):
        if line[i] == line[i + 2]:
            return True
    return False


def check_duplicates(line):
    for i in range(len(line) - 1):
        check = line[i: i + 2]
        if check in line[i + 2:]:
            return True
    return False


with open("text_input/day5_naughty_or_nice.txt") as f:
    for i in f.readlines():
        if check_triple(i):
            if check_duplicates(i):
                nice_count += 1

    print(nice_count)
