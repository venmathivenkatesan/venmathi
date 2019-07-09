q=int(input())
w=[]
for h in range(0,q):
 pan=input()
 w.append(pan)
thissss=[]
for h in zip(*w):
 if(h.count(h[0])==len(h)):
  ven.append(h[0])
 else:
  break
print(''.join(ven))
