n=int(input())
m=int(input())
line=[i for i in range(1,n+1)]
for i in range(m):
    stu,pos=map(int,input().split())
    after=line.index(stu)+pos
    line.remove(stu)
    line.insert(after,stu)
print(' '.join(map(str,line)))