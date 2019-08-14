a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
arr=[]
art=0
for i in range(a):
    xt=d[i]/c[i]
    arr.append(xt)
while b>=0 and len(arr)>0:
    mindex=arr.index(max(arr))
    if b>=c[mindex]:
        art=art+d[mindex]
        b=b-c[mindex]
    c.pop(mindex)
    d.pop(mindex)
    arr.pop(mindex)
print(art)
