import math

n=eval(input())
li=list(map(int,input().split()))
result=[]
for i in range(len(li)):
    if i==0:
        result.append(math.floor((li[i]+li[i+1])/2))
    elif i==len(li)-1:
        result.append(math.floor((li[i]+li[i-1])/2))
    else:
        result.append(math.floor((li[i-1]+li[i]+li[i+1])/3))
for i in result:
    print(i,end=' ')