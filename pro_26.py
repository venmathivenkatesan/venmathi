def subb(m): 
    ven = len(m) 
    subb = [1]*ven
    for i in range (1 , ven): 
        for j in range(0 , i): 
            if m[i] > m[j] and subb[i]< subb[j] + 1 : 
                subb[i] = subb[j]+1
    maximum = 0
    for i in range(ven): 
        maximum = max(maximum , subb[i])  
    return maximum
ar1=int(input()) 
m = list(map(int,input().split()))
print (subb(m))
