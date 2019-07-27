import math
v,n=map(int,input().split())
g=[]
bbb=list(map(int,input().split()))
for k in range(0,n):
    vn,asf=map(int,input().split())
    g.append([vn,asf])
for k in g:
    ven=k[0]-1
    thi=k[1]-1
    print(math.gcd(bbb[ven],bbb[thi]))
