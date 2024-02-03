n = int(input())
m = int(input())
o = int(input())

def judge(n,m,o):
    if n + m + o != 180:
        return print("Error")
    if n == m and m == o:
        return print("Equilateral")
    if n == m or m == o or n == o :
        return print("Isosceles")
    return print("Scalene")

judge(n,m,o)