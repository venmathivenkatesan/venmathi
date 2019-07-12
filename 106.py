v1,v2=map(int,input().split())
char=input().split()
d=[]
for h in char:
	if(int(h)%2!=0):
		d.append(h)
print(d[v2-1])
