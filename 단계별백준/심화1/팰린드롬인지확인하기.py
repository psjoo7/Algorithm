word = str(input())
wordLength = len(word)

if wordLength == 1:
    print("1")
else:
    i, j = 0, wordLength-1
    answer = 1
    while(i < j):
        if word[i] != word[j]:
            answer = 0
            break
        else:
            i += 1
            j -= 1
    print(answer)