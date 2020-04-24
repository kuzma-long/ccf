n,m=map(int,input().split())
wd,pm,tap,res=[],[],[],[]
for i in range(n):
    t1=tuple(map(int,input().split()))
    t2=(i+1,)
    t=t1+t2
    wd.append(t)
    pm+=[i+1]
for i in range(m):
    tap.append(tuple(map(int,input().split())))
for i in range(m):
    exist=[]
    for j in range(len(wd)):
        if (wd[j][0]<=tap[i][0]<=wd[j][2]) and (wd[j][1]<=tap[i][1]<=wd[j][3]):
            exist+=[int(wd[j][4])]
    if len(exist)==1:
        res+=[exist[0]]
        pm.append(exist[0])
        pm.remove(exist[0])
    elif len(exist)==0:
        res+=["IGNORED"]
    else:
        if pm[-1] in exist:
            res+=[pm[-1]]
        else:
            pos=[]
            for x in range(len(exist)):
                pos+=[pm.index(exist[x])]
            y=pm[max(pos)]
            res+=[y]
            pm.append(y)
            pm.remove(y)
for i in res:
    print(i)