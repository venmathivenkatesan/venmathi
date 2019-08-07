ven=int(input())
bob12=list(map(int,input().split()))
v1=max(bob12)
a,b=0,0
for o in range(0,len(bob12)-1):
  for p in range(o+1,len(bob12)):
    if abs(bob12[o]+bob12[p])<v1:
      c,d=bob12[o],bob12[p]
      v1=abs(a+b)
print(a,b)
