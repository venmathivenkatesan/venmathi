vv1=list(map(str,input()))
set1=g1=0
for k in range(0,len(vv1)-1):
  p=vv1[k]
  if int(p)!=0:
   for j in range(k+1,k+2):
    p=p+vv1[j]
    if int(p)<27 and int(p)>0: set1=set1+1
    elif int(p)==0: set1=set1-1
    else: break
if set1!=1: g1=set1%2
print(set1+g1+1)
