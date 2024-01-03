c1 = str(input())
c2 = str(input())

coor1 = c1.split(" ")
coor2 = c2.split(" ")
x = abs(int(coor2[0]) - int(coor1[0]))
y = abs(int(coor2[1]) - int(coor1[1]))

print(x+y)
