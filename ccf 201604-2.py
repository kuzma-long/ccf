tmap=[]
for i in range(15):
    tmap.append(list(map(int,input().split())))
for i in range(3):
    tmap.append([1]*10)
shape=[]
for i in range(4):
    shape.append(list(map(int,input().split())))
x=int(input())
for i in range(4):
    shape[i]=[0]*(x-1)+shape[i]+[0]*(10-4-(x-1))
right=0
find=False
for i in range(15):
    for j in range(4):
        newline=[a+b for a,b in zip(tmap[i+j],shape[j])]
        if (2 in newline):
            right=i-1
            find=True
            break
    if (i==14):
        right=14
    if find:
        break
for j in range(4):
    tmap[right+j]=[a+b for a,b in zip(tmap[right+j],shape[j])]
for i in range(15):
    print(' '.join(map(str,tmap[i])))