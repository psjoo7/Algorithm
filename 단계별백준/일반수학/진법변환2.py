alpha = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
         15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P',
         26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}

n, b = map(int, input().split())
answer = []
i = 0
while True:
    temp = b ** i
    if n / temp < b:
        break
    i += 1

for i in range(i, -1, -1):
    temp = b ** i
    share, remain = n // temp, n % temp
    answer.append(alpha[share])
    n = remain

for i in range(len(answer)):
    print(answer[i], end='')
