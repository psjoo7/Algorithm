mathlist = ['+', '-', '*', '/']

answer_list = []

def nCr(n, ans, r):
    if n == len(mathlist):
        if len(ans) == r:
            temp = [i for i in ans]
            answer_list.append(temp)
        return

    ans.append(mathlist[n])
    nCr(n+1, ans, r)
    ans.pop()
    nCr(n+1, ans, r)

nCr(0, [] , 3)
print(answer_list)