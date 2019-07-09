g = int(input())
m = []
for d in range(g):
	       m.append(input())
b = p[0]
m.remove(b)
o = len(b)
for d in m:
	       while o > 0:
	              	if b in d:
	                     		break
	              	o-=1
	              	b = b[:o]
print(b)
