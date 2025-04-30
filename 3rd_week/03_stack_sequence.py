def stack_sequence(n, sequence):
    stack = []
    num = 1
    sequence_index = 0
    result = []

    while True:
        if len(stack) == 0:
            stack.append(num)
            result.append('+')
            num += 1
        elif sequence[sequence_index] == stack[-1]:
            stack.pop()
            result.append('-')
            num += 1
            if sequence_index == n:
                break
        else:
            if n < num:
                print("NO")
                break
            else:
                stack.append(num)
                result.append('+')
                num += 1
    if len(stack) == 0:
        for char in result:
            print(char)
sequence = list()
n = int(input())
for _ in range(n):
    sequence.append(int(input()))
stack_sequence(n, sequence)