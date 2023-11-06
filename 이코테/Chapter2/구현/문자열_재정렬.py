array = list(input())

strArr = []
totalInt = 0

for i in array:
    try:
        totalInt += int(i)
    except:
        strArr.append(i)

strArr.sort()
strArr.append(totalInt)

for i in strArr:
    print(i, end="")