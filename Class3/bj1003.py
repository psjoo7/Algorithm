# 피보나치 함수
# 입력 : 테스트 케이스 T / 각 테스트 케이스 N
# 출력 : 0이 출력되는 횟수 / 1이 출력되는 횟수

# fibo(1) : 1을 리턴함. fibo(0) : 0을 리턴함.
import sys
input = sys.stdin.readline()
sys.setrecursionlimit(1000000)

T = int(input) # 테스트 케이스 T
testcases = [int(input) for _ in range(T)]
print(testcases)
# 메모이제이션 사용 ( DP )
dic = {1:1}

def fibo(n):
    global zero, one
    if n == 0:
        dic[0] = 0
        zero += 1
        return 0
    elif n == 1:
        dic[1] = 1
        one += 1
        return 1
    else:
        dic[n] = fibo(n-1) + fibo(n-2)
        return dic[n]

for i in testcases:
    zero = 0
    one = 0
    fibo(i)
    print(zero, end=" ")
    print(one)