import math
T=int(input())
salary=[3500,3500+1500,3500+4500,3500+9000,3500+35000,3500+55000,3500+80000,3500+100000]
cost=[0,3,10,20,25,30,35,45]
indeed=[]
s=T
for i in range(len(salary)):
    if i!=0:
        a+=(salary[i]-salary[i-1])*(1-cost[i]/100)
    else:
        a=3500
    indeed.append(int(a))
for i in range(len(salary)):
    if T<=indeed[i]:
        for j in range(i):
            s+=(salary[j]-salary[j-1])*(cost[j]/100)
        k=i
        break
s=(s-salary[k-1]*cost[k]/100)/(1-cost[k]/100)
print(math.ceil(s))