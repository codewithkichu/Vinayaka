#Exam Result Processing

n = int(input("Enter number of students: "))

distinction = 0
pass_count = 0
fail = 0

for i in range(1, n + 1):
    marks = int(input(f"\nEnter marks of Student {i}: "))

    if marks >= 75:
        print("Result: Distinction")
        distinction += 1
    elif marks >= 50:
        print("Result: Pass")
        pass_count += 1
    else:
        print("Result: Fail")
        fail += 1

print("\n------------------------------")
print("Total Distinction:", distinction)
print("Total Pass:", pass_count)
print("Total Fail:", fail)