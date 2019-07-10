vm=int(input())
for gh in range(2,vm):
    if vm%gh==0:
        print("no")
        break
else:
    print("yes")
