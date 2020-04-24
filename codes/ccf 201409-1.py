n=int(input())
a=list(map(int,input().split()))
a.sort()
count=0
for i in range(n-1):
    if(a[i+1]-a[i]==1):
        count+=1
print(count)