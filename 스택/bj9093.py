n = int(input())

for i in range(n):
    string = input()
    string += " "
    stack = []
    for j in string:
        if j != " ":
            stack.append(j)
        else :
            while stack:
                print(stack.pop(), end='')
            print(' ', end="")
    print()