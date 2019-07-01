v = int(input())
if v > 1:
   for i in range(2,v):
       if (v % i) == 0:
           print("no")
           break
   else:
       print("yes")
else:
   print("no")
