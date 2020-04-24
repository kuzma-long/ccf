def takenum(mlist):
    rlist=[]
    for x in mlist:
        if(x.isdigit()):
            rlist.append(int(x))
    return rlist
isbn=input()
l=takenum(isbn)
out=0
for i in range(9):
    out+=l[i]*(i+1)
code=out%11
if isbn[-1]==str(code) or (isbn[-1]=='X' and code==10):
    print("Right")
else:
    if code!=10:
        isbn=isbn[:-1]+str(code)
    else:
        isbn=isbn[:-1]+'X'
    print(isbn)