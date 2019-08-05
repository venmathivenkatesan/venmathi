V=int(input())
n1=input(" ")
n1=list(s1.split(' '))
d={}
for i in n1:
   if i in d:
      d[i]+=1
   else:
      d[i]=1
for key,value in d.items():
  if value==1:
     print(key)
