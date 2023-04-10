n = int(input())

for i in range(n):
    string = input()
    stack = []
    for j in string:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()
    if len(stack) != 0:
        print('NO')
    else: print("YES")