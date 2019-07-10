v,m=map(int,input().split())
if(v>m):
  t=v
else:
  t=m
while(True):
  if((t%v) == 0 and (t%m) == 0):
    lcm=t
    break
  t=t+1
print(lcm)
