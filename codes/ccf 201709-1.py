# def solve(n):
#     if n<50:
#         if n<30:
#             return n//10
#         else:
#             return 4+(n-30)//10
#     else:
#         return max(4+solve(n-30),7+solve(n-50))
# n=eval(input())
# print(solve(n))

n=eval(input())
x1=n//50
n%=50
x2=n//30
n%=30
x3=n//10
print(7*x1+4*x2+x3)