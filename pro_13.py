v, n = map(int,input().split())
arr=list(map(int,input().split()))
vn=[]
for j in range(g):
    c, d = map(int,input().split())
    vn.append([c,d])
tem=[]
for j in vn:
    v1=j[0]-1
    v2=j[1]
    for j in arr[v1:v2]:
        tem.append(i)
    print(min(tem))
    tem=[]
