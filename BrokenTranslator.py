import math
x = str(input())
digit=[]
for i in range(len(x)):
    digit.append([x[i],len(x)-i-1])
sum = 0
for i in digit:
    multiply = int(math.pow(2,int(i[1])))
    sum = sum + (int(i[0])*multiply)

print(sum)
    