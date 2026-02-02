# magic box number 
n=int(input("enter a number: "))
a=n
sum=0
while(a>0) :
    sum=sum+a%10
    a=a/10
print("Magic box number= ", sum)