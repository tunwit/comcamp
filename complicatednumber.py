p = int(input("ใส่ค่า :"))

if (p % 2) == 0:
    if (p % 4) == 0:
        print(1)
    else:
        print(-1)
else:
    p -= 1
    if (p % 4) == 0:
        print("i")
    else:
        print("-i")
            

