c1 = str(input())
c2 = str(input())

coor1 = c1.split(" ")
coor2 = c2.split(" ")

width = float(coor2[0]) - float(coor1[0])
high = float(coor2[1]) - float(coor1[1])

print(abs(width*high))