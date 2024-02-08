import sys

input = sys.stdin.readline

n = int(input())

array = dict()

for i in range(n):
    name, status = input().split()
    array[name] = status

answer = [key for key, value in array.items() if value == 'enter']
answer.sort(reverse=True)
for i in answer:
    print(i)

# array = dict()
# for _ in range(n):
#     name, status = input().split()
#     if status == 'enter':
#         array[name] = status
#     else:
#         del array[name]
#
# answer = sorted(list(array.keys()), reverse=True)
# print(*answer, sep='\n')