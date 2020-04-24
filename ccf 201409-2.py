counter=0
n=int(input())
mp=[[0]*100 for i in range(100)]
for i in range(n):
    m=tuple(map(int,input().split()))
    for j in range(m[3]-m[1]):
        for x in range(m[2]-m[0]):
            mp[m[0]+x][m[1]+j]=1
for i in range(100):
    for j in range(100):
        if mp[i][j]==1:
            counter+=1
print(counter)