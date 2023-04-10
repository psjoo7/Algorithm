#오름차순 정렬
a = [1, 5, 7, 4, 6]
a.sort()
print("오름차순 정렬 : ", a)
b = sorted(a) #a를 변경시키지 않을 수 있다.

#내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬 : ", a)

#정렬기준 정하기
#if y좌표만 정렬의 기준으로 하고 싶다면,
#정렬의 기준을 인자로 정해주면 됨
x = [list(map(int, input().split())) for _ in range(5)]
x.sort(key=lambda x:x[1])
print("y좌료 기준으로 정렬 : ", x)

#1. y좌표를 오름차순으로
#2. y좌표가 같다면 x좌표를 내림차순으로
y = [list(map(int, input().split())) for _ in range(5)]
y.sort(key=lambda y:(y[1], -y[0]))
print("1. y좌표를 오름차순으로 \ny좌표가 같다면 x좌표를 내림차순으로\n", y)