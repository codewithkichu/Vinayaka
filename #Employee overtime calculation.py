#Employee overtime calculation

n = int(input("Enter number of employees: "))

total_overtime = 0

for i in range(1, n + 1):
    hours = int(input(f"\nEnter overtime hours of Employee {i}: "))

    if hours <= 5:
        pay = 0
    elif hours <= 10:
        pay = 500
    else:
        pay = 1000

    print(f"Overtime Pay for Employee {i}: ₹{pay}")
    total_overtime += pay

print("\n------------------------------")
print("Total Overtime Amount: ₹", total_overtime)