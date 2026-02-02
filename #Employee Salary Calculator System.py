#Employee Salary Calculator System

# Function to input employee details
def get_employee_details():
    name = input("Enter Employee Name: ")
    emp_id = input("Enter Employee ID: ")
    basic_salary = float(input("Enter Basic Salary: "))
    return name, emp_id, basic_salary


# Function to calculate gross salary
def calculate_gross_salary(basic_salary):
    hra = basic_salary * 0.20
    da = basic_salary * 0.10
    gross_salary = basic_salary + hra + da
    return gross_salary, hra, da


# Function to calculate deductions
def calculate_deductions(basic_salary, gross_salary):
    pf = basic_salary * 0.12
    tax = gross_salary * 0.05
    total_deductions = pf + tax
    return total_deductions, pf, tax


# Function to display final salary
def display_salary(name, emp_id, basic, gross, deductions, net, hra, da, pf, tax):
    print("\n------ Salary Slip ------")
    print("Employee Name:", name)
    print("Employee ID:", emp_id)
    print("Basic Salary: ₹", basic)
    print("HRA: ₹", hra)
    print("DA: ₹", da)
    print("Gross Salary: ₹", gross)
    print("PF Deduction: ₹", pf)
    print("Tax Deduction: ₹", tax)
    print("Total Deductions: ₹", deductions)
    print("Net Salary: ₹", net)
    print("-------------------------")


# Main Program
def main():
    name, emp_id, basic_salary = get_employee_details()

    gross_salary, hra, da = calculate_gross_salary(basic_salary)

    deductions, pf, tax = calculate_deductions(basic_salary, gross_salary)

    net_salary = gross_salary - deductions

    display_salary(name, emp_id, basic_salary, gross_salary,
                   deductions, net_salary, hra, da, pf, tax)


# Run program
main()