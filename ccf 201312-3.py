n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(len(a)):
    width=0
    for j in reversed(range(i)):
        if a[j]>=a[i]:
            width+=1
        else:
            break
    for j in range(i,len(a)):
        if a[j]>=a[i]:
            width+=1
        else:
            break
    b.append(a[i]*width)
print(max(b))