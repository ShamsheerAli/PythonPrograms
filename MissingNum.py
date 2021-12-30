num=list(input("Enter the numbers: "))
num=sorted(num)
for j in range(0,len(num)):
    num[j]=int(num[j])
print(num)
for i in reversed(range(1,len(num))):
    if num[i]-num[i-1]!=1:
     missing=num[i-1]+1
     print(missing)     
