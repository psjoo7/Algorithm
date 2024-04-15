word = input()
s = list(input())
answer = []

for i in range(len(word)):
    answer.append(word[i])
    if len(answer) < len(s):
        continue
    else:
        if answer[len(answer)-len(s):] == s:
            del answer[len(answer)-len(s):]

if answer == []:
    print("FRULA")
else:
    print(''.join(answer))