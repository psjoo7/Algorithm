array = []
maxLen = 0
for i in range(5):
    wordList = str(input())
    if maxLen < len(wordList):
        maxLen = len(wordList)
    array.append(wordList)

for i in range(maxLen):
    for j in range(5):
        if len(array[j]) <= i:
            continue
        else:
            print(array[j][i], end="")
