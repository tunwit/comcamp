fibo = ["0","1"]
for i in range(100):
    fibo.append(str(int(fibo[-1:][0])+int(fibo[-2:][0])))

i = int(input())

for i in range(i):
    result = ' '.join(fibo[:i+1])
print(result)
