lst = []
for i in range(3):
    lst.append(int(input()))
    
for i in range(3):
    m = min(lst)
    lst.remove(m)
    print(m)
