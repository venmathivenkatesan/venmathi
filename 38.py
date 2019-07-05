v,m=map(int,input("").split())
v=v ^ m
m=v ^ m
v=m ^ v
print(v,m)
