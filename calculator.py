def add(n1,n2): 
    return n1+n2
def sub(n1,n2):
    return n1-n2 
def mul(n1,n2):
    return n1*n2 
def div(n1,n2):
    return n1/n2          

operators={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
num1=int(input("Enter The First Number"))
num2=int(input("Enter The Second Number"))
for i in operators:
    print(i)
operator=input("Enter The Operator")
func=operators[operator]
print(func(num1,num2))