import aocd


def part_one():
    lines = aocd.get_data(year=2022, day=2).split("\n")
    score = 0

    for line in lines:
        choices = line.split(" ")
        match choices[1]:
            case 'X':
                score += 1
                match choices[0]:
                    case 'A':
                        score += 3
                    case 'C':
                        score += 6
            case 'Y':
                score += 2
                match choices[0]:
                    case 'A':
                        score += 6
                    case 'B':
                        score += 3
            case 'Z':
                score += 3
                match choices[0]:
                    case 'B':
                        score += 6
                    case 'C':
                        score += 3

    return score


def part_two():
    lines = aocd.get_data(year=2022, day=2).split("\n")
    score = 0

    for line in lines:
        choices = line.split(" ")
        match choices[1]:
            case 'X':
                match choices[0]:
                    case 'A':
                        score += 3
                    case 'B':
                        score += 1
                    case 'C':
                        score += 2
            case 'Y':
                score += 3
                match choices[0]:
                    case 'A':
                        score += 1
                    case 'B':
                        score += 2
                    case 'C':
                        score += 3
            case 'Z':
                score += 6
                match choices[0]:
                    case 'A':
                        score += 2
                    case 'B':
                        score += 3
                    case 'C':
                        score += 1

    return score


def main():
    print(part_one())
    print(part_two())


if __name__ == '__main__':
    main()