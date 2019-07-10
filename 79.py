vv1,mm2=map(int,input().split())
dd3=vv1*mm2
for g in range(0,dd3+1):
 if(g**2==0):
  print("yes")
  break
else:
  print("no")
