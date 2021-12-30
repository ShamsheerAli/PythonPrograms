num=input("Enter the number: ")
list1=list(num)
for j in range(0,len(list1)):
    list1[j]=int(list1[j])
print(list1)
count=0
for i in reversed(range(0,len(list1))):
    if list1[i]==0:
        count+=1
        if list1[i-1]!=0:
          break
        
print(count)        
       