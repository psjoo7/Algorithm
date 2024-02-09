import sys
input = sys.stdin.readline

def ans(a,b):
    if a < b :
        a , b = b , a
    if a % b == 0:
        return b
    return ans(b, a%b)

aTop, aBottom = map(int, input().split())
bTop, bBottom = map(int, input().split())

def getAns(aTop, aBottom, bTop, bBottom):
    if aBottom == 1:
        return aTop * bBottom + bTop, bBottom
    if bBottom == 1:
        return aBottom * bTop + aTop, aBottom

    minBe = (aBottom * bBottom) // ans(aBottom, bBottom)

    bunmo = (minBe // aBottom) * aTop + (minBe // bBottom) * bTop

    return bunmo, minBe

bunmo, minBe = getAns(aTop,aBottom,bTop,bBottom)
temp = ans(bunmo, minBe)
bunmo, minBe = bunmo // temp, minBe // temp
print(bunmo, minBe)