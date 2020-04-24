n=int(input())
now=input()
print('\n',end='')
for i in range(0,n):
    dir=input()
    if dir=='':
        print(now+'\n')
        continue
    if dir[0]!='/':
        dir=now+'/'+dir
    dir=dir.replace('/',' ')
    dir=dir.split()
    ans=[]
    for x in dir:
        if x=='.':
            continue
        elif x=="..":
            if len(ans)!=0:
                ans.pop()
        else:
            ans.append(x)
    print('/',end='')
    for i in range(0,len(ans)):
        if i!=0:
            print('/',end='')
        print(ans[i],end='')
    print('\n',end='')