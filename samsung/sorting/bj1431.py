n = int(input())
a = [input() for _ in range(n)]

def sum_num(inputs):
    result = 0
    for i in inputs:
        if i.isdigit():
            result += int(i)
    return result

a.sort(key=lambda x:(len(x), sum_num(x), x))

for _ in a:
    print(_)