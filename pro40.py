ven1="dhoni"
ven2=input()
pop1=list(set(ven1)-set(ven2))
pop2=list(set(ven2)-set(ven1))
pop=len(pop1)+len(pop2)
if pop==0:
	print("yes")
else:
	print("no")
