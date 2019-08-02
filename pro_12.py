v,n=map(int,input().split())
nv=list(map(int,input().split()))
l1=[]
for i in range(0,n):
     c,d=map(int,input().split())
     l1.append([c,d])
for j in range(n):
     lower=l1[i][0]
     upper=l1[i][1]
     y=sum(nv[lower-1:upper])
     print(y)
