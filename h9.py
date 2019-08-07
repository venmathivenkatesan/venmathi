ven=int(input())
bob11=list(map(int,input().split()))
g1=max(bob11)
a,b=0,0
for o in range(0,len(bob11)-1):
  for p in range(o+1,len(bob11)):
    if abs(bob11[o]+bob11[p])<g1:
      a,b=bob11[o],bob11[p]
      g1=abs(a+b)
print(a,b)
