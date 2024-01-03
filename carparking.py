import math

mins = int(input())
hour = math.ceil(mins/60)
price = 0
if mins <= 15:
    pass
if hour >= 2:
    price = price + (30)
if hour > 2 :
    if hour > 24:
        price = price + (760)
    else:
        price = price + (30*(hour-2))
print(price)