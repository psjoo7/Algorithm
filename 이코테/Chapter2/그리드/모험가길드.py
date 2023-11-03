n = int(input())

fear = list(map(int, input().split()))
fear.sort()

count = 0
standard = fear[0]
for i in range(n-1):
    standard -= 1
    if standard == 0:
        count += 1
        standard = fear[i+1]

print(count)