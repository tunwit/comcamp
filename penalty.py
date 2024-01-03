x = int(input())
q = ["$"]
for i in range(x-1):
    if q[i] == "$":
        q.append("#")
    else:
        q.append("$")
print(''.join(q))
        