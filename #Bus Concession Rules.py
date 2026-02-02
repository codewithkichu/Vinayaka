#Bus Concession Rules

PASS_FEE = 1000

n = int(input("Enter number of students: "))

concession_50 = 0
concession_25 = 0
no_concession = 0

for i in range(1, n + 1):
    age = int(input(f"\nEnter age of Student {i}: "))

    if age < 18:
        discount = PASS_FEE * 0.50
        payable = PASS_FEE - discount
        concession_50 += 1
        category = "50% Concession"
    elif age <= 25:
        discount = PASS_FEE * 0.25
        payable = PASS_FEE - discount
        concession_25 += 1
        category = "25% Concession"
    else:
        discount = 0
        payable = PASS_FEE
        no_concession += 1
        category = "No Concession"

    print(f"Category: {category}")
    print(f"Payable Amount: ₹{payable}")

print("\n------------------------------")
print("Students with 50% Concession:", concession_50)
print("Students with 25% Concession:", concession_25)
print("Students with No Concession:", no_concession)