#Shopping Discount System
n = int(input("Enter number of customers:"))
discount_count = 0
for i in range(1 ,n+1):
    bill =float(input(f"\nEnter the bill amount of Customer {i}:"))
    if bill >= 5000:
        discount = bill * 0.20
        discount_count += 1
    elif bill >= 2000:
        discount = bill * 0.10
        discount_count += 1
    else:
        discount = 0
    final_amount = bill - discount
    print(f"Discount : {discount} /-")
    print(f"Final Bill Amount : {final_amount}/-")
    print("\n-----------------------------")
    print("Number of customers who received discount:",discount_count)