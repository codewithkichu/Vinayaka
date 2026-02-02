#Salary Bonus Distributions

n = int(input("Enter the number of employees"))
total_bonus = 0
for i in range(1 , n+1):
    salary = float(input(f"\nEnter the salary of Employee{i}:/-"))
    years = int(input(f"Enter years of service of Employee {i}:/-"))
    if years >= 10:
        bonus = salary * 0.20
    elif years >= 5:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05

    print(f"Bonus for Employee {i}:{bonus}/-")
    total_bonus += bonus
    print("\n----------------------------")
    print("Total bonus Paid:",total_bonus,"/-")
