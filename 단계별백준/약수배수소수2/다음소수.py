import sys
input = sys.stdin.readline

t = int(input())

def find(a):
    if a == 0 or a == 1:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

for _ in range(t):
    number = int(input())
    while True:
        if find(number):
            print(number)
            break
        number += 1