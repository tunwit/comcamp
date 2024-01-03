need = int(input())
sen = []
for i in range(need):
    sen.append(str(input()))
ns = []
for s in sen:
    new = []
    if s[0].isupper():
        new.append(s[0])
    else:
        new.append(s[0].upper())
    for i in range(len(s)-1):
        if new[i].isupper():
            cha = s[i+1].lower()
        elif new[i].islower():
            cha = s[i+1].upper()
        elif new[i].isupper() is False and new[i].islower() is False:
            if new[i-1].isupper():
                cha = s[i+1].lower()
            else:
                cha = s[i+1].upper()
        new.append(cha)
    ns.append(''.join(new))

for i in ns:
   print(i)

