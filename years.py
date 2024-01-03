amount = []
do = True
for money in range(2):
    m = int(input())
    if m > 200000:
        print("Input Error")
        do = False
        break
    elif m == 0:
        break
    amount.append(m)
if do:
    a = sum(amount)
    t = a//1000
    a = abs((1000*t)-a)
    f = a//500
    a = abs((500*f)-a)
    h = a//100
    a = abs((100*h)-a)
    print(t)
    print(f)
    print(h)