a=[]
sum=0
weight=1
x=input()
for i in x.split():
    a.append(eval(i))
for i in range(len(a)):
    if a[i]==1:
        weight=1
    elif a[i]==2:
        if weight==1:
            weight=2
        else:
            weight+=2
    elif a[i]==0:
        break
    sum+=weight
print(sum)