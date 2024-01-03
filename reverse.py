word = input()
num = len(word)
new= []
for i in range(num):
    if i == 0:
        new.append(word[-1])
    else:
        new.append(word[-i-1])
print(''.join(new))
