# n=int(input())
# matrix=[]
# for i in range(n):
#     l=list(map(int,input().split()))
#     matrix.append(l)
# i=0
# j=0
# print(matrix[i][j],end=" ")
# flag="right"
# while True:
#     if flag=="right":
#         j+=1
#         if i==0:
#             flag="left-down"
#         if i==n-1 and j==n-1:
#             print(matrix[i][j],end=" ")
#             break
#         if i==n-1:
#             flag="right-up"
#         print(matrix[i][j],end=" ")
#     if flag=="down":
#         i+=1
#         if j==0:
#             flag="right-up"
#         if j==n-1:
#             flag="left-down"
#         print(matrix[i][j],end=" ")
#     if flag=="left-down":
#         i+=1
#         j-=1
#         if j==0:
#             flag="down"
#         if i==n-1:
#             flag="right"
#         if i!=n-1 and j!=0:
#             flag="left-down"
#         print(matrix[i][j],end=" ")
#     if flag=="right-up":
#         i-=1
#         j+=1
#         if j==n-1:
#             flag="down"
#         if i==0:
#             flag="right"
#         if j!=n-1 and i!=0:
#             flag="right-up"
#         print(matrix[i][j],end=" ")

n=int(input())
rect=[]
for i in range(n):
    rect.append(list(map(int,input().split())))
i,j=0,0
line=[]
up=True
for t in range(n*n):
    line.append(rect[j][i])
    if up:
        if i==n-1:
            j+=1
            up=False
        elif j==0:
            i+=1
            up=False
        else:
            j-=1
            i+=1
    else:
        if j==n-1:
            i+=1
            up=True
        elif i==0:
            j+=1
            up=True
        else:
            i-=1
            j+=1
print(' '.join(map(str,line)))