n=int(input())
a=list(map(int,input().split()))
b=[1]*n
for i in range(n):
    for j in range(i+1,n):
        if(a[j]==a[i]):
            b[j]+=1
for item in b:
    print(item,end=" ")