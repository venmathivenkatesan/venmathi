vm,g=map(int,input().split())
s=list(map(int,input().split()[:vm]))
for o in range(0,vm):
    if s[o]==g:
        print("yes")
        break
else:
    print("no")
