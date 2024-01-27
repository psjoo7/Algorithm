# testcase = int(input())
# for i in range(testcase):
#     word = str(input())
#     wordLength = len(word)
#     print(word[0], end="")
#     print(word[wordLength-1])

testcase = int(input())
for i in range(testcase):
    word = str(input())
    print(word[0]+word[-1])