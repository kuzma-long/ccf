a=input()
c=input()
cnt=int(input())
test=[]
for i in range(cnt):
    test.append(input())
if c=='0':
    a=a.lower()
for tt in test:
    cc=tt
    if c=='0':
        cc=cc.lower()
    if a in cc:
        print(tt)