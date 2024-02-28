n = int(input())

def fib_je(n):
    num = 1
    if n == 1 or n == 2:
        return 1
    else:
        return fib_je(n-1) + fib_je(n-2)

def fib_dp(n):
    f = [1,1]
    num = 0
    for i in range(2, n):
        num += 1
        f.append(f[i-1] + f[i-2])
    return f[n-1], num

je, dp = fib_dp(n)
print(je, dp)