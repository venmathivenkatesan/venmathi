vm=input()
for r in range(0,len(vm)):
    
    if (vm[r].isalpha() and vm[r].isnumeric()):
        print("No")
else:
        print("Yes")
