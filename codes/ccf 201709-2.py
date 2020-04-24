n,k=map(int,input().split())
keys=[i for i in range(1,n+1)]
datas=[]
for i in range(k):
    temp=list(map(int,input().split()))
    datas.append([temp[0],temp[1],1])
    datas.append([temp[0],temp[1]+temp[2],2])
datas.sort(key=lambda temp:(temp[1],-temp[2],temp[0]))
for i in datas:
    if i[2]==1:
        keys[keys.index(i[0])]=0
    else:
        keys[keys.index(0)]=i[0]
for i in keys:
    print(i,end=' ')