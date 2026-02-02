#Payroll Management System

employees = {}   # Stores employee payroll data

# Function to add employee data
def add_employee(emp_id, name, base_salary):
    employees[emp_id] = {
        "name": name,
        "base_salary": base_salary
    }
    print("✅ Employee added successfully!")

# Function to calculate salary dynamically
def calculate_salary(base_salary, bonus=0, deduction=0):
    return base_salary + bonus - deduction

# Function to handle bonus and deductions (flexible call)
def process_payroll(emp_id, bonus=0, deduction=0):
    if emp_id not in employees:
        print("❌ Employee not found!")
        return

    base = employees[emp_id]["base_salary"]
    final_salary = calculate_salary(base, bonus, deduction)

    employees[emp_id]["bonus"] = bonus
    employees[emp_id]["deduction"] = deduction
    employees[emp_id]["final_salary"] = final_salary

    print("✅ Payroll processed!")

# Function to generate payroll report
def generate_report():
    if not employees:
        print("❌ No employee data available.")
        return

    print("\n📊 Payroll Report")
    print("-------------------------")
    for emp_id, data in employees.items():
        print("ID:", emp_id)
        print("Name:", data["name"])
        print("Base Salary: ₹", data["base_salary"])
        print("Bonus: ₹", data.get("bonus", 0))
        print("Deduction: ₹", data.get("deduction", 0))
        print("Final Salary: ₹", data.get("final_salary", data["base_salary"]))
        print("-------------------------")

# Main program
def main():
    while True:
        print("\n--- Payroll Management System ---")
        print("1. Add Employee")
        print("2. Process Payroll")
        print("3. Generate Report")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            salary = float(input("Enter Base Salary: "))
            add_employee(emp_id, name, salary)

        elif choice == "2":
            emp_id = input("Enter Employee ID: ")
            bonus = float(input("Enter Bonus (default 0): ") or 0)
            deduction = float(input("Enter Deduction (default 0): ") or 0)
            process_payroll(emp_id, bonus, deduction)

        elif choice == "3":
            generate_report()

        elif choice == "4":
            print("👋 Exiting Payroll System")
            break

        else:
            print("❌ Invalid choice!")

# Run program
main()