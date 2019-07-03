o=int(input())
gxd=list(map(int,input().split()[:o]))
gxd.sort()
for v in gxd:
  print(v,end=" ")
