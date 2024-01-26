total = int(input())
productNumber = int(input())

productList = []
productTotal = 0

for i in range(productNumber):
    productList.append(list(map(int,input().split())))

for i in range(productNumber):
    productTotal += productList[i][0] * productList[i][1]

if len(productList) != productNumber:
    print("No")
elif total != productTotal:
    print("No")
else:
    print("Yes")