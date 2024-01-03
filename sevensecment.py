def zero():
    lst = [
        ["000"],
        ["0 0"],
        ["0 0"],
        ["0 0"],
        ["000"],
        ]
    return lst

def one():
    lst = [
        ["  0"],
        ["  0"],
        ["  0"],
        ["  0"],
        ["  0"],
        ]
    return lst
def two():
    lst = [
        ["000"],
        ["  0"],
        ["000"],
        ["0  "],
        ["000"],
        ]
    return lst
    
def three():
    lst = [
        ["000"],
        ["  0"],
        ["000"],
        ["  0"],
        ["000"],
        ]
    return lst

def four():
    lst = [
        ["0 0"],
        ["0 0"],
        ["000"],
        ["  0"],
        ["  0"],
        ]
    return lst

def five():
    lst = [
        ["000"],
        ["0  "],
        ["000"],
        ["  0"],
        ["000"],
        ]
    return lst

def six():
   lst = [
        ["000"],
        ["0  "],
        ["000"],
        ["0 0"],
        ["000"],
        ]
   return lst

def seven():
    lst = [
        ["000"],
        ["  0"],
        ["  0"],
        ["  0"],
        ["  0"],
        ]
    return lst

def eight():
    lst = [
        ["000"],
        ["0 0"],
        ["000"],
        ["0 0"],
        ["000"],
        ]
    return lst

def nine():
    lst = [
        ["000"],
        ["0 0"],
        ["000"],
        ["  0"],
        ["000"],
        ]
    return lst

dic = {
    '0':"zero",
    '1':"one",
    '2':"two",
    '3':"three",
    '4':"four",
    '5':"five",
    '6':"six",
    '7':"seven",
    '8':"eight",
    '9':"nine",
    }
x = input()
n=[]
for i in range(len(x)):
    n.append(x[i])
q = []
for i in n:
    q.append(eval(f"{dic[i]}()"))

l = []
for i in range(5):
  l.append([j[i][0] for j in q])

for i in range(5):
    print(' '.join(l[i]))
    
    

    