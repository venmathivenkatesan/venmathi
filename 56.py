kl=input()
for p in range(0,len(kl)):
    
    if (kl[p].isalpha() and kl[p].isnumeric()):
        print("No")
else:
        print("Yes")
