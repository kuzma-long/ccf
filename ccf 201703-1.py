n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
f = 0
nowk = 0
for i in a:
    nowk += i
    if nowk >= k:
        nowk = 0
        f += 1
if nowk != 0:
    f += 1
print(f)