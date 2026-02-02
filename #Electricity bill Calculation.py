#Electricity bill Calculation

n = int(input("Enter the number of consumers :"))
total_collection = 0
for i in range(1,n+1):
    units = int(input(f"\nEnter units consumed by Consumer{i}:"))
    if units <= 100:
        bill = units * 2
    elif units <= 300:
        bill = units * 3
    else:
        bills = units * 5
    print(f"Bills for consumers {i}:{bill}/-")
    total_collection += bill
    print("\n----------------------")
    print("Total amount collected : ",total_collection,"/-")