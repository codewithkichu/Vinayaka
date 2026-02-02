#Bank Loan Eligibility


n = int(input("Enter number of customers: "))

high_count = 0
medium_count = 0
not_eligible = 0

for i in range(1, n + 1):
    income = int(input(f"\nEnter annual income of Customer {i}: ₹"))

    if income >= 500000:
        print("Loan Category: High Loan")
        high_count += 1
    elif income >= 300000:
        print("Loan Category: Medium Loan")
        medium_count += 1
    else:
        print("Loan Category: Not Eligible")
        not_eligible += 1

eligible = high_count + medium_count

print("\n------------------------------")
print("High Loan Customers:", high_count)
print("Medium Loan Customers:", medium_count)
print("Not Eligible Customers:", not_eligible)
print("Total Eligible Customers:", eligible)