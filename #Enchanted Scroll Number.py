#Enchanted Scroll Number 
n=int(input("Enter a number:"))
sum=n
a=n
while sum>9:
    a=sum
    sum=0
    while a>1:
        sum=sum+a%10
        a=a/10
if sum==1:
    print(n,"is a Enchant scroll number")
else:
     print(n," is not Enchant scroll number ")