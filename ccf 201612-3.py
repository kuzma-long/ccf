line=input()
n=int(line)
au=[]
for i in range(0,n):
    tt=input()
    au.append(tt)
line=input()
n=int(line)
xx={}
for i in range(0,n):
    tt=input()
    tt=tt.split(' ')
    tt.remove(tt[1])
    bas=[]
    for ii in tt[1:]:
        if(':' in ii):
            ii=ii.split(':')
            gg=int(ii[1])
            if ii[0] not in bas:
                bas.append(ii[0])
            for j in range(gg,-1,-1):
                add=ii[0]+':'+str(j)
                if add not in bas:
                    bas.append(add)
        else:
            bas.append(ii)
    xx[tt[0]]=bas
line=input()
n=int(line)
user={}
for i in range(0,n):
    tt=input()
    tt=tt.split(' ')
    tt.remove(tt[1])
    basic=[]
    for lit in tt[1:]:
        basic.append(xx[lit])
    user[tt[0]]=basic
line=input()
n=int(line)
for i in range(0,n):
    cc=input()
    cc=cc.split(' ')
    if(cc[0] in user):
        o=0
        flag=False
        zz=0
        if(':' in cc[1]):
            for auth in user[cc[0]]:
                if(cc[1] in auth):
                    o+=1
                    if(o>=1):
                        break
        else:
            kk=cc[1]+':'+str(zz)
            for auth in user[cc[0]]:
                if kk in auth:
                    flag=True
                    while kk in auth:
                        kk=cc[1]+':'+str(zz)
                        zz+=1
                else:
                    if cc[1] in auth:
                        o+=1
        if(flag):
            print(str(zz-2))
        elif o>=1:
            print('true')
        else:
            print('false')
    else:
        print('false')