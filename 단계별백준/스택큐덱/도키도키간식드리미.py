import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
numList = deque(map(int,input().split()))
waitingList = []
frontNumber = 1
while 1:
    # 입력줄 체크
    if len(numList) != 0 and numList[0] == frontNumber:
        numList.popleft()
        frontNumber += 1
    # 대기줄 체크
    if len(waitingList) != 0 and waitingList[-1] == frontNumber:
        waitingList.pop()
        frontNumber += 1
    if frontNumber > n:
        break
    # 둘 다 안되는 경우, 입력줄에서 대기줄로 숫자 옮기기
    if len(numList) != 0:
        if len(waitingList) == 0:
            waitingList.append(numList.popleft())
        else:
            if numList[0] > waitingList[-1]:
                if numList[0] == frontNumber:
                    numList.popleft()
                    frontNumber += 1
                if len(waitingList) != 0 and waitingList[-1] == frontNumber:
                    waitingList.pop()
                    frontNumber += 1
                else:
                    print("Sad")
                    break
            else:
                waitingList.append(numList.popleft())

if len(waitingList) == 0 and len(numList) == 0:
    print('Nice')