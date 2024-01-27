n = int(input())

answer = 0
for i in range(n):
    word = str(input())
    char = "1"
    array = []
    flag = 1
    for j in range(len(word)):
        if char != word[j]:
            char = word[j]
            if char in array:
                flag = 0
                break
            else:
                array.append(char)
    if flag == 1:
        answer += 1

print(answer)