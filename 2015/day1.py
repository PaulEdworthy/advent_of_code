# Part 1

with open('text_input/day1_parens.txt') as f:
    buf = f.read()

opening = buf.count('(')
closing = buf.count(')')
print(opening - closing)

# Part 2
total = 0
position = 0
for i in buf:
    position += 1
    if i == '(':
        total += 1
    elif i == ')':
        total -= 1
    if total == -1:
        break
print(position)
