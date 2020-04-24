list1=[[1,0],[-1,0],[0,1],[0,-1]]
list2=['-','|','+','XXX']
def bfs(x,y,c):
    for i in list1:
        xx=i[0]+x
        yy=i[1]+y
        if xx>=n or xx<0 or yy>=m or yy<0 or artwork[yy][xx] in list2:
            continue
        artwork[yy][xx]=c
        bfs(xx,yy,c)
n,m,p=map(int,input().split())
artwork=[['.'for i in range(n)]for j in range(m)]
for i in range(p):
    list3=input().split()
    if int(list3[0])==0:
        list3=[int(x) for x in list3]
        if list3[1]==list3[3]:
            for j in range(min(list3[2],list3[4]),max(list3[2],list3[4])+1):
                if artwork[j][list3[1]]=='+' or artwork[j][list3[1]]=='-':
                    artwork[j][list3[1]]='+'
                else:
                    artwork[j][list3[1]]='|'
        else:
            for j in range(min(list3[1],list3[3]),max(list3[1],list3[3])+1):
                if artwork[list3[2]][j]=='+' or artwork[list3[2]][j]=='|':
                    artwork[list3[2]][j]='+'
                else:
                    artwork[list3[2]][j]='-'
    else:
        list2[3]=list3[3]
        bfs(int(list3[1]),int(list3[2]),list3[3])
for i in range(m):
    for j in artwork[m-1-i]:
        print(j,end='')
    print()