v,m=map(str,input().split())
gh=0
if len(v)>len(m):
  v,m=m,v
c=0
while c<len(v):
  gh+=(ord(m[c])-ord(v[c]))
  c+=1
for c in range(c,len(m)):
  gh+=ord(m[c])-ord('b')+1
print(gh)
