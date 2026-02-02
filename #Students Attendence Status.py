#Students Attendence Status

n = int(input("Enter number of students: "))

eligible = 0
conditional = 0
not_eligible = 0

for i in range(1, n + 1):
    attendance = float(input(f"\nEnter attendance percentage of Student {i}: "))

    if attendance >= 85:
        print("Status: Eligible for Exam")
        eligible += 1
    elif attendance >= 75:
        print("Status: Conditionally Eligible")
        conditional += 1
    else:
        print("Status: Not Eligible")
        not_eligible += 1

print("\n------------------------------")
print("Eligible Students:", eligible)
print("Conditionally Eligible Students:", conditional)
print("Not Eligible Students:", not_eligible)