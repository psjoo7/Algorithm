input_list = [1,2,3,4,5]
used = [0] * len(input_list)
# 순열 : 순서가 다르면 다른 경우의 수
def perm(arr, n):
    if n == len(input_list):
        print(arr)
        return
    for i in range(len(input_list)):
        if not used[i]:
            used[i] = 1
            arr.append(input_list[i])
            perm(arr, n+1)
            arr.pop()
            used[i] = 0

perm([], 2)

# 조합 : 순서가 달라도 같은 경우의 수
answer_list = []
def combi(n, ans):
    if n == len(input_list):
        temp = [i for i in ans]
        answer_list.append(temp)
        return
    ans.append(input_list[n])
    combi(n + 1, ans)
    ans.pop()
    combi(n + 1, ans)

combi(0, [])
print(answer_list)

# nCr : 주어진 리스트에서 r개의 값을 나열하는 경우의 수
answer_list = []
def nCr(n, ans, r):
    if n == len(input_list):
        if len(ans) == r:
            temp = [i for i in ans]
            answer_list.append(temp)
        return
    ans.append(input_list[n])
    nCr(n + 1, ans, r)
    print(ans.pop())
    nCr(n + 1, ans, r)

nCr(0, [], 3)
print(answer_list)