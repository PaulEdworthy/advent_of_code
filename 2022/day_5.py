
with open('text_input/day_5.txt', 'r') as f:
    # for line in f:
    #     print(line,end='')

    header = f.read().splitlines()[0:9]
    # data = f.read().splitlines()[10:]
    stack = []
    stack4 = []
    stack6 = []
    count = 8
    for i in range(count):
        count -= 1
        stack.append(header[count][1])
        stack4.append(header[count][13])
        stack6.append(header[count][21])
    print(stack)
    print(stack4)
    print(stack6)