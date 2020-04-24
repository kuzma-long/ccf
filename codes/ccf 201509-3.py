import re
line=[int(v) for v in input().split()]
i=0
kk={}
ht={}
for j in range(line[0]):
    html=input()
    g=re.findall(r"{{ (.+?) }}",html)
    for x in g:
        s='{{ '
        s+=x
        s+=' }}'
        kk[s]=''
    ht[i]=html
    i+=1
for j in range(line[1]):
    a,b=input().split(' ',1)
    b=b.strip('"')
    s='{{ '
    s+=a
    s+=' }}'
    if s in kk:
        kk[s]=b
for j in range(len(ht)):
    for a,b in kk.items():
        if a in ht[j]:
            ht[j]=ht[j].replace(a,b)
    print(ht[j])