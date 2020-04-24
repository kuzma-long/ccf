n=int(input())
p1=[[0,30]]
p2=[[0,30]]
now=1
for i in range(0,n):
    x=input()
    if x[0]=='s':
        x=x.split()
        p=int(x[1])
        a=int(x[2])
        h=int(x[3])
        if now==1:
            p1.insert(p,[a,h])
        else:
            p2.insert(p,[a,h])
    if x[0]=='a':
        x=x.split()
        a=int(x[1])
        d=int(x[2])
        if now==1:
            p2[d][1]-=p1[a][0]
            p1[a][1]-=p2[d][0]
            if p1[a][1]<=0 and a!=0:
                p1.remove(p1[a])
            if p2[d][1]<=0 and d!=0:
                p2.remove(p2[d])
        else:
            p1[d][1]-=p2[a][0]
            p2[a][1]-=p1[d][0]
            if p2[a][1]<=0 and a!=0:
                p2.remove(p2[a])
            if p1[d][1]<=0 and d!=0:
                p1.remove(p1[d])
    if x[0]=='e':
        if now==1:
            now=2
        else:
            now=1
if p1[0][1]>0 and p2[0][1]>0:
    print('0')
elif p1[0][1]<=0 and p2[0][1]>0:
    print('-1')
elif p1[0][1]>0 and p2[0][1]<=0:
    print('1')
print(p1[0][1])
print(len(p1)-1,end=' ')
for i in range(1,len(p1)):
    print(p1[i][1],end=' ')
print('\n',end='')
print(p2[0][1])
print(len(p2)-1,end=' ')
for i in range(1,len(p2)):
    print(p2[i][1],end=' ')
print()