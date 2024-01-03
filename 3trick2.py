glass = [1,0,0]

for i in range(5):
    select = input()

    if select == 'A':
        glass[0],glass[1] = glass[1],glass[0]
    elif select == 'B':
        glass[1],glass[2] = glass[2],glass[1]
    elif select == 'C':
        glass[0],glass[2] = glass[2],glass[0]

if glass[0] == 1:
    print(1)
elif glass[1] == 1:
    print(2)
elif glass[2] == 1:
    print(3)