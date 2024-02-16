import sys
input = sys.stdin.readline

while 1:
    string = input().rstrip()
    if string == ".":
        break
    if string[-1] != ".":
        print('no')
        continue
    smallFlag = 0
    bigFlag = 0
    isSmallOrBig = []
    isNo = 0

    for i in string:
        if i == '(':
            smallFlag += 1
            isSmallOrBig.append('small')
        if i == ')':
            smallFlag -= 1
            if len(isSmallOrBig) != 0 and isSmallOrBig.pop() == 'big':
                isNo = 1
        if i == '[':
            bigFlag += 1
            isSmallOrBig.append('big')
        if i == ']':
            bigFlag -= 1
            if len(isSmallOrBig) != 0 and isSmallOrBig.pop() == 'small':
                isNo = 1

        if smallFlag < 0 or bigFlag < 0:
            isNo = 1
            break
    if len(isSmallOrBig) != 0 :
        isNo = 1
    if isNo:
        print('no')
        continue
    print('yes')
