#Modular Reporting System

# ---------------------------
# Independent Report Functions
# ---------------------------

def sales_report():
    print("\n📈 Sales Report")
    print("Total Sales: ₹50,000")
    print("Top Product: Laptop")

def employee_report():
    print("\n👨‍💼 Employee Report")
    print("Total Employees: 25")
    print("Present Today: 22")

def inventory_report():
    print("\n📦 Inventory Report")
    print("Available Items: 320")
    print("Low Stock Items: 12")


# ---------------------------
# Central Report Registry
# ---------------------------

report_registry = {
    "sales": sales_report,
    "employee": employee_report,
    "inventory": inventory_report
}


# ---------------------------
# Central Function to Call Reports
# ---------------------------

def generate_report(report_name):
    report_function = report_registry.get(report_name)

    if report_function:
        report_function()    # Call selected report
    else:
        print("❌ Report not found!")


# ---------------------------
# Main Program
# ---------------------------

def main():
    print("\nAvailable Reports:")
    for name in report_registry:
        print("-", name)

    choice = input("\nEnter report name: ").lower()
    generate_report(choice)


# Run program
main()