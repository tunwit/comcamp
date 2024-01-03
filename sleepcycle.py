cycle = [
    [0,"Awake"],
    [5,"1st Phase"],
    [15,"2nd Phase"],
    [60,"3rd Phase"],
    [10,"REM Phase"],
]
m = int(input())
h = int(input())
htm = 0
if h !=0:
    htm =60*h
totalm = htm+m
count = 0
while totalm > 0 :
    if count > 3:
        count = 0
    totalm -= cycle[count+1][0]
    count+=1
print(cycle[count][1])
