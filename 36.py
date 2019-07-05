mathi1=input()
l1=0
for v in range(len(mathi1)):
  if(mathi1[v].isdigit() or mathi1[v].isalpha() or mathi1[v]==(" ")):
    continue
  else:
    l1+=1
print(l1)
