# n = int(input())
# a = list(map(int, input().split()))
# t = [0] * 20
# for x in a:
#     find = False
#     for i in range(20):
#         if 5 - t[i] - x >= 0:
#             start = i * 5 + t[i] + 1
#             t[i] += x
#             for y in range(start, start + x):
#                 print(y, end=' ')
#             print()
#             find = True
#             break
#     if not find:
#         for i in range(20):
#             if x > 0 and t[i] < 5:
#                 start = i * 5 + t[i] + 1
#                 length = 5 - t[i]
#                 if x > length:
#                     x -= length
#                     t[i] = 5
#                     for y in range(start, start + length):
#                         print(y, end=' ')
#                 else:
#                     t[i] += x
#                     for y in range(start, start + x):
#                         print(y, end=' ')
#                     print()
#                     x = 0
#                     break

n=int(input())
lst=list(map(int,input().split()))
line=[0]*20
for p in lst:
    find=False
    for i in range(20):
        if 5-line[i]>=p:
            start=5*i+line[i]+1
            line[i]+=p
            find=True
            for j in range(start,start+p):
                print(j,end=' ')
            print()
            break
    if not find:
        for i in range(20):
            if p>0 and line[i]<5:
                start = 5 * i + line[i] + 1
                if line[i] + p > 5:
                    line[i] = 5
                    p -= (5 - line[i])
                    for j in range(start, 5 * (i + 1) + 1):
                        print(j, end=' ')
                else:
                    line[i]+=p
                    p=0
                    for j in range(start,start+p):
                        print(j,end=' ')
                    print()
                    break