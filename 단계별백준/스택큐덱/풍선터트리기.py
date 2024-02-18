n = int(input())
array = list(map(int, input().split()))
start = 0
index = [_ for _ in range(1, n+1)]
answer = []
temp = array.pop(start)
answer.append(index.pop(start))

while array:
    if temp < 0 :
        start = (start + temp) % len(array)
    else:
        start = (start + temp - 1) % len(array)
    temp = array.pop(start)
    answer.append(index.pop(start))

for i in answer:
    print(i, end=" ")