key = int(input())
sen = str(input())

al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
new = []

for i in sen:
    if i.isspace() == False:
        index = al.index(i) + key
        if index > 25:
            index = index-26
        new.append(al[index])
    else:
        new.append(i)
print(''.join(new))
    

#ABCDEFGHIJKLMN OPQRSTUVWXYZ