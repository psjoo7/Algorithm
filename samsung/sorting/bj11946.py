n, m, q = map(int, input().split())
acm_icpc = [[[301, 0] for _ in range(m+1)] for _ in range(n+1)]

for _ in range(q):
    time, team, prob, result = input().split()
    time = int(time)
    team = int(team)
    prob = int(prob)

    if acm_icpc[team][prob][0] == 301:
        if result == 'AC':
            acm_icpc[team][prob][0] = time
        else :
            acm_icpc[team][prob][1] += 20

grade = [[i, 0, 0] for i in range(n+1)]

for team in range(1, n+1):
    for prob in range(1, m+1):
        if acm_icpc[team][prob][0] != 301:
            grade[team][1] += 1
            grade[team][2] += acm_icpc[team][prob][0]
            grade[team][2] += acm_icpc[team][prob][1]

grade = sorted(grade[1:], key=lambda x:(-x[1], x[2], x[0]))
for i in grade:
    print(i[0], i[1], i[2])