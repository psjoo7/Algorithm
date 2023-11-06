n = list(map(int, input()))

arrlen = len(n)
mid = int(arrlen / 2)

left = 0
right = 0

for i in range(mid):
    left += n[i]
    right += n[i+mid]

if left == right:
    print("LUCKY")
else:
    print("READY")