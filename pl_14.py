#v
v=input()
b=str(input())
c=('a','e','i','o','u')
for j in b:
    if j in c:
        b=b.replace(j,"")
print(b[::-1])
