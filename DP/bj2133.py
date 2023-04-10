# N = int(input())
# T = [0] * (N+1)
#
# for i in range(1, N + 1):
#     if i % 2 != 0:
#         T[i] = 0
#     elif i == 2:
#         T[2] = 3
#     else:
#         for j in range(1, i//2):
#             T[i] = T[2*j] * T[i-(2*j)]
# print(T[N])

n = int(input())
T = [0 for i in range(31)]
T[2] = 3
for i in range(4, 31, 2):
    T[i] = T[2] * T[i - 2]
    for j in range(4, i, 2):
        T[i] += 2 * T[i - j]
    T[i] += 2
print(T[n])