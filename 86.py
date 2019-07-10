asd=list(input())
ven=[]
for k in asd:
   if k not in ven:
      ven.append(k)
if asd==ven:
   print("Yes")
else:
   print("No")
