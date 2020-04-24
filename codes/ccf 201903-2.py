n=int(input())
exps=[]
for i in range(n):
    exps.append(input())
for i in range(n):
    numStack = []
    opStack = []
    exp=exps[i]
    for a in exp:
        if a=='+' or a=='-' or a=='x' or a=='/':
            opStack.append(a)
        elif opStack:
            if opStack[-1]=='x':
                arg=numStack.pop()
                numStack.append(arg*int(a))
                opStack.pop()
            elif opStack[-1]=='/':
                arg=numStack.pop()
                numStack.append(arg//int(a))
                opStack.pop()
            else:
                numStack.append(int(a))
        else:
            numStack.append(int(a))
    for op in opStack:
        arg0=numStack.pop(0)
        arg1=numStack.pop(0)
        numStack.insert(0,arg0+arg1 if op=='+' else arg0-arg1)
    if numStack[0]==24:
        print('YES')
    else:
        print('NO')