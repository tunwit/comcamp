x = str(input())
new = []
for i in range(len(x)):
    new.append(x[-(i+1)])
newsen = ''.join(new)
if newsen == x:
    print("Yes")
else:
    print("No")
    
