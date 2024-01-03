ac = int(input())

speed = (ac*30)
if speed >= 90:
    if speed > 100:
        print(speed)
        print(500+((speed-100)*100))
elif speed >= 60 and speed < 90:
    print(200)
elif speed >= 30 and speed < 60:
    print(100)
