n = int(input())
a = list(range(1, n+1))
a.reverse()
stack1 = []
stack2 = []
answer = []
for i in range(n):
    word = int(input())
    while len(a) > 0 and word >= a[-1]:
        stack1.append(a.pop())
        answer.append('+')
    if stack1[-1] == word:
        stack2.append(stack1.pop())
        answer.append('-')
    elif stack1[-1] != word:
        answer = 'NO'
        break
if answer == 'NO':
    print(answer)
else :
    for x in range(len(answer)):
        print(answer[x])