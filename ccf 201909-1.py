n,m=list(map(int,input().split()))
sum=0
c=[]
for i in range(n):
    line=list(map(int,input().split()))
    a=line[0]
    b=0
    for j in range(m):
        a+=line[j+1]
        b-=line[j+1]
    sum+=a
    c.append(b)
max=0
maxid=0
for i in range(len(c)):
    if c[i]>max:
        max=c[i]
        maxid=i+1
print(sum,maxid,max)