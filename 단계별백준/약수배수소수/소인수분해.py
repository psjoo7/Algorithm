# # 소수 판별 함수
# def is_sosu(num):
#     if num == 1:
#         return False
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True
#
# n = int(input())
# array = []
# while True:
#     if n == 1:
#         break
#     for i in range(2, n + 1):
#         if n % i == 0 and is_sosu(i):
#             array.append(i)
#             n //= i
#             break
#
# for i in array:
#     print(i)

n = int(input())
i = 2
sqrt = int(n**0.5)

while i <= sqrt:
    if n % i == 0:
        n /= i
        print(i)
    else:
        i += 1

if n > 1:
    print(int(n))