# a=[]
# n=eval(input())
# li=input().split()
# for i in li:
#     a.append(eval(i))
# a.sort()
# minnum=999999
# i=1
# while i<n:
#     minnum=min(minnum,a[i]-a[i-1])
#     i=i+1
# print(minnum)

n=eval(input())
li=list(map(int,input().split()))
li.sort()
difference=list(map(lambda x,y:y-x,li[:-1],li[1:]))
print(min(difference))