temp = 3 ** 12
s = 3 ** 12
array = ['-'] * temp

while temp != 1:
    a = temp // 3
    x = 0
    while temp * x <= s:
        array[temp * x + a: temp * x + a * 2] = " " * a
        x += 1
    temp //= 3

f = []
while True:
    try:
        n = input()
        t = 3 ** int(n)
        f.append(t)
    except EOFError:
        break

for i in f:
    for j in range(i):
        print(array[j], end='')
    print()