#GCD
import math
q=[]
v,m=map(int,input().split())
q1=list(map(int,input().split()))
for x in range(m):
    e,r=map(int,input().split())
    q.append([e,r])
for y in q:
     c1=y[0]-1
     c2=y[1]-1
     print(math.gcd(q1[c1],q1[c2]))
