v,m=map(int,input().split())
for r in range(v+1,m):
  ch=r
  fnd=0
  while(r>0):
   d=r%10
   fnd=fnd+(d**3)
   r=r//10
   if(fnd==ch):
      print(fnd,end=" ")
