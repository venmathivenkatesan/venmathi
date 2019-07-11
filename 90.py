vm=input()
j=[]
for t in vm:
	if t.isnumeric():
		j.append(t)
print(''.join(j))
