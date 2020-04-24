n,L,t=input().split()
line=input().split()
x=int(n)
count=[]
addr=[]
for i in range(x):
    count.append(1)
for i in range(x):
    addr.append(int(line[i]))
for i in range(int(t)):
    for s in range(x):
        if addr[s]==0 or addr[s]==int(L):
            count[s]=-count[s]
    for j in range(x):
        for k in range(j+1,x):
            if addr[j]==addr[k]:
                count[j]=-count[j]
                count[k]=-count[k]
    for z in range(x):
        addr[z]=addr[z]+count[z]
for i in range(len(addr)):
    print(addr[i],end='\t')