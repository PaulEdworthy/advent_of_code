# Part 1

visited = [(0, 0)]  # the starting point
x = y = 0
count = 1

with open("text_input/day3_spherical.txt") as f:
    for c in f.read().strip():
        match c:
            case '^':
                y += 1
            case '>':
                x += 1
            case 'v':
                y -= 1
            case '<':
                x -= 1

        if (x, y) not in visited:
            visited.append((x, y))
            count += 1
f.close()
print(f"Part 1 count: {count}")

# Part 2

both_visited = [(0, 0)]
santa_x = santa_y = robo_x = robo_y = 0
santa = True
count = 1  # The starting point is a house


with open("day3_spherical.txt") as f:
    for c in f.read().strip():

        if santa:
            match c:
                case '^':
                    santa_y += 1
                case '>':
                    santa_x += 1
                case 'v':
                    santa_y -= 1
                case '<':
                    santa_x -= 1

            if (santa_x, santa_y) not in both_visited:
                both_visited.append((santa_x, santa_y))
                count += 1

            santa = False

        else:
            match c:
                case '^':
                    robo_y += 1
                case '>':
                    robo_x += 1
                case 'v':
                    robo_y -= 1
                case '<':
                    robo_x -= 1

            if (robo_x, robo_y) not in both_visited:
                both_visited.append((robo_x, robo_y))
                count += 1

            santa = True

print(f"Part 2 count: {count}")  # 2472 was too low
