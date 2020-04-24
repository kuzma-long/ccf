n=int(input())
drop=[0]*n
sum=0
num=0
for i in range(n):
    line=list(map(int,input().split()))
    m=line[0]
    a=line[1]
    for j in range(m-1):
        b=line[j+2]
        if b<=0:
            a+=b
        else:
            if (a-b)>0:
                drop[i]=1
                num+=1
                a=b
    sum+=a
team=0
for i in range(len(drop)):
    if i==len(drop)-1:
        if drop[i-1]+drop[i]+drop[0]==3:
            team+=1
    else:
        if drop[i-1]+drop[i]+drop[i+1]==3:
            team+=1
print(sum,num,team)