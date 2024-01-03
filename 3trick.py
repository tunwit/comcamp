seq = []
for i in range(5):
    seq.append(input())

ball = [1,0,0]

for i in seq:
    if i == 'A':
        if ball[0] == 1 and ball[1] == 0:
            ball[0] = 0
            ball[1] = 1
        elif ball[0] == 0 and ball[1] == 1:
            ball[0] = 1
            ball[1] = 0
    elif i == 'B':
        if ball[1] == 1 and ball[2] == 0:
            ball[1] = 0
            ball[2] = 1
        elif ball[1] == 0 and ball[2] == 1:
            ball[1] = 1
            ball[2] = 0
    elif i == 'C':
        if ball[2] == 0 and ball[0] == 1:
            ball[2] = 1
            ball[0] = 0
        elif ball[2] == 1 and ball[0] == 0:
            ball[2] = 0
            ball[0] = 1

if ball.index(1) == 0:
    print(1)
if ball.index(1) == 1:
    print(2)
if ball.index(1) == 2:
    print(3)
