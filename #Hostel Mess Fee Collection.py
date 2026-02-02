#Hostel Mess Fee Collection

FULL_FEE = 3000

n = int(input("Enter number of students: "))

full_count = 0
seventyfive_count = 0
fifty_count = 0

for i in range(1, n + 1):
    attendance = float(input(f"\nEnter attendance percentage of Student {i}: "))

    if attendance >= 90:
        fee = FULL_FEE
        full_count += 1
        category = "Full Fee"
    elif attendance >= 75:
        fee = FULL_FEE * 0.75
        seventyfive_count += 1
        category = "75% Fee"
    else:
        fee = FULL_FEE * 0.50
        fifty_count += 1
        category = "50% Fee"

    print(f"Category: {category}")
    print(f"Mess Fee to Pay: ₹{fee}")

print("\n------------------------------")
print("Students paying Full Fee:", full_count)
print("Students paying 75% Fee:", seventyfive_count)
print("Students paying 50% Fee:", fifty_count)