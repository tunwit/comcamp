import math

staff = str(input()).split(" ")
amount = str(input()).split(" ")
days = []
for i in range(2):
    if i == 0:
        mul = 6
    else:
        mul = 10
    devider = int(staff[i])*mul
    if staff[i] != "0" or amount[i] != "0":
        try:
            day = int(amount[i]) / int(devider)
        except:
            print("Unable to finish order")
            break
        days.append(math.ceil(day))


try:
    if len(days) == 1 and days[0] == 0:
        i = 1/0
    print(max(days))
except:pass

    