n,m=map(int,input().split())
bmap=[]
amap=[[0]*m for i in range(n)]
for i in range(n):
    bmap.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if (i>0 and i<n-1 and bmap[i][j]==bmap[i-1][j] and bmap[i][j]==bmap[i+1][j]):
            amap[i-1][j]=1
            amap[i][j]=1
            amap[i+1][j]=1
        if (j>0 and j<m-1 and bmap[i][j]==bmap[i][j-1] and bmap[i][j]==bmap[i][j+1]):
            amap[i][j-1]=1
            amap[i][j]=1
            amap[i][j+1]=1
for i in range(n):
    for j in range(m):
        if (amap[i][j]==1):
            bmap[i][j]=0
        print(bmap[i][j],end=' ')
    print()