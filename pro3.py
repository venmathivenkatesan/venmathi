v,m=input().split()
jk=abs(len(m)-len(v))
for g in range(len(v)):
    if(len(m)==1 and m[g] in v):
        break
    if (v[g]!=m[g]):
        jk=jk+1
print(jk)
