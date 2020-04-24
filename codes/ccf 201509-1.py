n=int(input())
a=list(map(int,input().split()))
count=1
last=a[0]
for item in a:
    if(item!=last):
        count+=1
    last=item
print(count)