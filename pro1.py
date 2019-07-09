ven=int(input())
k=[]
for w in range(0,ven):
 as=input()
 k.append(as)
new=[]
for w in zip(*k):
 if(w.count(w[0])==len(w)):
  new.append(w[0])
 else:
  break
print(''.join(new))
