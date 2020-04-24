# def check(a,n):
#     sum=0
#     for i in range(n):
#         if a[i]==0:
#             sum=sum+1
#     if sum==1:
#         return False
#     else:
#         return True
# i=0
# sum=0
# n,k=input().split()
# n=eval(n)
# k=eval(k)
# a=[0]*n
# while check(a,n):
#     if a[i]==0:
#         sum=sum+1
#     if sum%k==0 or sum%10==k:
#         a[i]=1
#     i=i+1
#     if i==n:
#         i=0
# for i in range(n):
#     if a[i]==0:
#         print(i+1)

n,k=input().split()
n=int(n)
k=int(k)
count=[]
x=1
b=0
for i in range(n):
    count.append(1)
for i in range(10000):
    if sum(count)==1:
        break
    for j in range(n):
        if count[j]!=0:
            x+=1
        if ((x-1)%k==0 or (x-1-k)%10==0):
            count[j]=0
        if sum(count)==1:
            break
for j in range(n):
    if count[j]==1:
        b=j
print(b+1)