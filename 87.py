v3,g4=map(int,input().split())
d=1
while(d<=v3 and d<=g4):
 if(v3%d==0 and g4%d==0):
  gcd1=d
 d=d+1
print(gcd1)
