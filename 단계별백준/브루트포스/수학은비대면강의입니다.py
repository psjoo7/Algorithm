'''
ax + by = c
dx + ey = f
ea, eb, ec
db, eb, cb
'''
a,b,c,d,e,f = map(int,input().split())

x = (e*c - b*f)//(a*e - b*d)
y = (-d*c + a*f)//(a*e - b*d)

print(x, y)