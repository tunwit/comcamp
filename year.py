years = int(input())
if years%4 == 0:
    print("Yes")
elif years%100 == 0:
    print("No")
elif years%400 == 0 and years%100 == 0:
    print("No")
elif years%400 == 0 and years%100 != 0:
    print("Yes")
elif years%400 == 0:
    print("Yes")