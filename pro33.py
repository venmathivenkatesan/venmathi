ven=input()
for i in range(len(ven)):
  if(ven[i] < ven[i+1]):
    print(ven[i+1:])
    break
