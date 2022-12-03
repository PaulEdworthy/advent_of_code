import aocd
data = aocd.get_data(year=2022, day=2).split("\n")

def first():
    total = 0

    for line in data:
        choice = line.split(" ")
        match choice[1]:
            case 'X':
                total += 1
                match choice[0]:
                    case 'A':
                        total += 3
                    case 'C':
                        total += 6
            case 'Y':
                total += 2
                match choice[0]:
                    case 'A':
                        total += 6
                    case 'B':
                        total += 3
            case 'Z':
                total += 3
                match choice[0]:
                    case 'B':
                        total += 6
                    case 'C':
                        total += 3

    return total


def second():
    total = 0

    for line in data:
        choice = line.split(" ")
        match choice[1]:
            case 'X':
                match choice[0]:
                    case 'A':
                        total += 3
                    case 'B':
                        total += 1
                    case 'C':
                        total += 2
            case 'Y':
                total += 3
                match choice[0]:
                    case 'A':
                        total += 1
                    case 'B':
                        total += 2
                    case 'C':
                        total += 3
            case 'Z':
                total += 6
                match choice[0]:
                    case 'A':
                        total += 2
                    case 'B':
                        total += 3
                    case 'C':
                        total += 1

    return total


def main():
    print(first())
    print(second())


if __name__ == '__main__':
    main()