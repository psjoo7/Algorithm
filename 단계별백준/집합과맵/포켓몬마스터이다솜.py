'''
n - 도감에 수록되어 있는 포켓몬의 수
m - 맞춰야하는 문제의 수
(1 <= n,m <= 100,000)
'''
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
pokeList = {}
for i in range(n):
    poke = input().strip()
    pokeList[poke] = i+1
    pokeList[str(i+1)] = poke

for _ in range(m):
    print(pokeList[input().strip()])