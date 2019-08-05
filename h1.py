from collections import Counter
v1=int(input())
v2=list(map(int,input().split()))
v3=Counter(v2)
list=[]
for x in v3.items():
  if(x[1] != 1):
   print(x[0],end ='')
for y in v3.items():
  list.append(y[1])
if(max(list) == 1):
  print("unique")
