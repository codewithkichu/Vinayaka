#Iron Seal Number 
n=int(input(" Enter a code : "))
sum=0
a=n
dig=0
pro=1
while a>0:
    dig=(int)(a%10)
    for i in range(1,dig):
        pro=pro*i
    sum=sum+pro
    a=a/10
if sum== n:
    print("Gate Opens!!")
else:
    print("Gate closed!!!")