#Bus Ticket Inspector 
age=int(input("Enter age of the passenger "))
dis=int(input("Enter distance of travelling in km "))
amount=0
if age<=5:
    amount=0
elif age>5 and age<=18 :
    amount=dis*1.5
else:
    amount= dis*2.5
print("Amount = ", amount)
