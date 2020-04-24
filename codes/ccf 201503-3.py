day = [29, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month=list(range(1,13))
year=list(range(1850,2051))
data={}
week=2
i=0
for y in year:
    if ((y%4==0 and y%100!=0) or y%400==0):
        day[2]=day[0]
    for m in month:
        da=day[m]
        for d in range(1,da+1):
            data[i]=(y,m,d,week)
            week+=1
            week%=7
            i+=1
    day[2]=28
line=input().split(" ")
line=[int(v) for v in line]
line[2]%=7
a=False
i=0
k=0
while k<len(data):
    if (data[k][1]==line[0] and data[k][0]>=line[3] and data[k][0]<=line[4] and data[k][3]==line[2]):
        i+=1
        if i==line[1]:
            a=True
            print(str(data[k][0])+'/'+str('%0.2d'%data[k][1])+'/'+str('%0.2d'%data[k][2]))
    if (data[k][1]==12 and data[k][2]==31 and data[k][0]>=line[3] and data[k][0]<=line[4]):
        if a==False:
            print('none')
        i=0
        a=False
    k+=1