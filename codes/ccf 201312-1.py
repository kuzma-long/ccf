n=int(input())
a=list(map(int,input().split()))
b=list(set(a))
b.sort()
s=dict(zip(b,map(a.count,b)))
print(max(s,key=s.get))