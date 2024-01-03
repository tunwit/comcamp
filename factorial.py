import math
fac = str(input("ใส่ค่า P n r: "))
number = fac.split(" ")
n = math.factorial(int(number[0]))
r = math.factorial(int(number[1]))
print(n/r)
