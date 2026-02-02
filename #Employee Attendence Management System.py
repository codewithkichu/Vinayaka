#Employee Attendence Management System

attendance = {}   # Dictionary to store employee attendance

def mark_attendance():
    emp_id = input("Enter Employee ID: ")
    status = input("Enter Attendance (P for Present / A for Absent): ").upper()

    if status == "P" or status == "A":
        attendance[emp_id] = status
        print("✅ Attendance marked successfully!")
    else:
        print("❌ Invalid input! Please enter P or A.")

def calculate_working_days():
    present_days = 0
    for status in attendance.values():
        if status == "P":
            present_days += 1
    print("📅 Total Working Days (Present):", present_days)
    return present_days

def generate_attendance_report():
    if len(attendance) == 0:
        print("❌ No attendance data available.")
        return

    print("\n📊 Attendance Report")
    print("--------------------------")
    for emp_id, status in attendance.items():
        print("Employee ID:", emp_id, "| Status:", status)

    calculate_working_days()

def main():
    while True:
        print("\n--- Employee Attendance Management System ---")
        print("1. Mark Attendance")
        print("2. Calculate Working Days")
        print("3. Generate Attendance Report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            mark_attendance()
        elif choice == "2":
            calculate_working_days()
        elif choice == "3":
            generate_attendance_report()
        elif choice == "4":
            print("Thank you 👋")
            break
        else:
            print("❌ Invalid choice!")

# Program execution
main()