from collections import Counter
n=int(input())
number_list=list(map(int,input().split()))
p=Counter(number_list)
while True:
    times=0
    for v in p.values():
        if v>=times:
            times=v
    list_l=[]
    for k,v in p.items():
        if v==times:
            list_l.append(k)
    list_l.sort()
    for i in list_l:
        p.pop(i)
    for i in list_l:
        print(i,times)
    if len(p.keys())==0:
        break