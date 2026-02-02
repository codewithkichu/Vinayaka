#Friendly kingdom Numbers
m=int(input("Enter 1 number :"))
n=int(input("Enter second number :"))
s1=0
s2=0
for i in range(m):
    if m%i==0:
        s1+=i
for j in range(n):
    if n%j==0:
        s2+=j
if s1==s2:
    print(m," and ",n," are friendly partners")
else:
    print(m," and ",n," are not friendly partners")