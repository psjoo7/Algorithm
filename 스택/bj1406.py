import sys

stack1 = list(input())
N = int(input())

stack2 = []

for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'B':
        if len(stack1) != 0:
            stack1.pop()
    elif command[0] == 'L':
        if len(stack1) != 0:
            stack2.append(stack1.pop())
    elif command[0] == 'D':
        if len(stack2) != 0:
            stack1.append(stack2.pop())
    else:
        stack1.append(command[-1])

print(''.join(stack1 + list(reversed(stack2))))