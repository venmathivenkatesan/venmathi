ven=int(input())
n=input("")
n=list(n.split(" "))
g=[]
for v in range(0,len(n)):
  for u in range(v+1,len(n)):
    if n[v]==n[u]:
      g.append(n[v])
if(len(g)==0):
  print("unique")
else:
  print(g[0])
