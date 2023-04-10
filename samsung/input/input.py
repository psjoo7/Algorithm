#input()
a = input() # int(input())
print( "기본 : ", a )

#split()
b = input().split()
print( " split : " , b )

#map()
c = list(map(int, input().split()))
print( " map : " , c , " #주의 : list로 반드시 감싸주어야함")

#가변인자
x, *y = map(int, input().split())
print( " 가변인자 : ", *y )

#1차원 배열
z = [0] * 10 # z = [ 0 for _ in range(10) ]
print( " 1차원 배열 : ", z )

#2차원 배열
m, n = map(int, input().split())
i = [[0] * m for _ in range(n)]
print( " 2차원 배열 : ", i)