l_v = input().split(' ')
levels = int(l_v[0])
videos = int(l_v[1])

lst = []
for video in range(videos):
    l_t = input().split(' ')
    l = int(l_t[0])
    t = int(l_t[1])
    
    lst.append({
        "level":l,
        "time":t
    })

lst = sorted(lst,key=lambda x:x['time'])
lst = sorted(lst,key=lambda x:x['level'])

result = []
approve = []
for index,value in enumerate(lst):
    if index != 0:
        if value['level'] in approve:
            continue
    approve.append(value['level'])
    result.append(value)

sum_time = sum([i['time']for i in result])
print(sum_time)

for i in result:
    print(i['level'],i['time'])