rating = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

totalSubject = 0
totalGrade = 0

for i in range(20):
    subject, number, grade = input().split()
    if grade == 'P':
        continue
    else:
        totalSubject += float(number)
        totalGrade += float(number) * rating[grade]

if totalSubject == 0:
    print("0.000000")
else:
    print("{:.6f}".format(totalGrade/totalSubject))