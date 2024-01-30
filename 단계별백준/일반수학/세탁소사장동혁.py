peny = [25, 10, 5, 1]

t = int(input())
for i in range(t):
    answer = []
    change = int(input())
    for i in range(4):
        share, remain = change // peny[i], change % peny[i]
        change = remain
        answer.append(share)
    for i in range(4):
        print(answer[i], end=" ")
    print()

