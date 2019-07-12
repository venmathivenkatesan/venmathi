v,m=map(str,input().split())
if(len(v)!=len(m)):
    print("no")
else :
    f1=[v.count(j) for j in v]
    f2=[m.count(j) for j in m]
if(f1==f2):
    print("yes")
else:
    print("no")
