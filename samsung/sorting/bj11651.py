n = int(input())
answer = []
for _ in range(n):
    a = list(map(int, input().split()))
    answer.append(a)

answer.sort(key=lambda x:(x[1], x[0]))

for i in answer:
    for j in i:
        print(j, end=" ")
    print("")