ven,mathi=map(int,input().split())
anto=0
Liee14=[]
for i in range(ven):
      Liee14.append(input())
for i in range(ven):
      for q in range(mathi-1):
            if(Liee14[i][q]!='R' and Liee14[i][q+1]!='R'):
                  anto+=3
            elif(Liee14[i][q]!='G' and Liee14[i][q+1]!='G'):
                  anto+=5
print(anto)
