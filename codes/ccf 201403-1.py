n=int(input())
a=list(map(int,input().split()))
b=set(map(abs,a))
print(len(a)-len(b))