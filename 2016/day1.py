# starting point is facing North. Follow instructions to end.
# how many blocks from the start are you?
# R2, R2, R2 isn't 6 blocks from the start, it's 2

x = y = 0
direction = 'north'

with open('day1.txt') as f:
    buffer = f.readline()
    sp = buffer.split(', ')
    for d in sp:
        
        print(d)
