options=input()
n=int(input())
sop=[]
mop=[]
options+=' '
for i in range(len(options)-1):
    if (options[i+1]==':'):
        mop.append(options[i])
    elif (options[i]!=':'):
        sop.append(options[i])
for t in range(n):
    cmd=input().split()
    coption=dict()
    i=1
    while (i<len(cmd)):
        if (len(cmd[i])==2 and cmd[i][0]=='-'):
            if (cmd[i][1] in sop):
                coption[cmd[i][1]]=''
                i+=1
            elif (cmd[i][1] in mop and i+1<len(cmd)):
                coption[cmd[i][1]]=cmd[i+1]
                i+=2
            else:
                break
        else:
            break
    keys=list(set(coption.keys()))
    keys.sort()
    print("Case"+str(t+1)+':',end='')
    for key in keys:
        print(" -"+key,end='')
        if (coption[key]!=''):
            print(' '+coption[key],end='')
    print()