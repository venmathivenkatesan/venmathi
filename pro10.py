v=int(input())
n=[int(j) for j in input().split(" ")]
vn=0
for h in range(v):
      for i in range(h):
           if(n[i]<n[h]):
                vn+=n[i]
print(vn)
