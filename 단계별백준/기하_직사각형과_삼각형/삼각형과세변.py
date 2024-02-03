def judge(n,m,o):
    if n + m + o - max(n,m,o) <= max(n,m,o):
        return print("Invalid")
    if n == m and m == o:
        return print("Equilateral")
    if n == m or m == o or n == o :
        return print("Isosceles")
    return print("Scalene")

while True:
    n,m,o = map(int, input().split())
    if n == 0 and m == 0 and o == 0:
        break
    judge(n,m,o)

