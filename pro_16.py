ven1=int(input())
lis1=list(map(int,input().split()))
at=[1]*ven1
for vn in range(ven1):
    if(vn==0):
        if(lis1[vn]>lis1[vn+1]):
            at[vn]=at[vn]+at[vn+1]
    elif(vn>0):
        if(lis1[vn]>lis1[vn-1]):
            at[vn]=at[vn]+at[vn-1]
print(sum(at))
