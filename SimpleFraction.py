n=int(input("Enter The Numerator: "))
d=int(input("Enter The Denomirator: "))
z=(n/d)
z=str(z)
num=list(z)
print(num)
for i in range(0,len(num)):
    if num[i]=='.':
      j=i+1
print(j)  
for k in range(j,len(num)):
    li=num(k)
    if len(li)==1:
        num1=num[k]
    elif num[k]==num[k+1]:
     num1=num[k]
     break       
print(num1)
