n=int(input())
a=list(map(int,input().split()))
wave_max=0
for i in range(1,n):
    if abs(a[i]-a[i-1])>wave_max:
        wave_max=abs(a[i]-a[i-1])
print(wave_max)