#Configurable Billing Engine



# ---------------------------
# Tax Rule Functions
# ---------------------------

def india_tax(amount):
    return amount * 0.18   # 18% GST

def usa_tax(amount):
    return amount * 0.07   # 7% Sales Tax

def dubai_tax(amount):
    return amount * 0.05   # 5% VAT


# ---------------------------
# Core Billing Engine
# ---------------------------

def generate_bill(amount, tax_function):
    tax = tax_function(amount)     # Dynamic function call
    total = amount + tax

    print("\n🧾 Billing Summary")
    print("Base Amount: ₹", amount)
    print("Tax: ₹", round(tax, 2))
    print("Total Amount: ₹", round(total, 2))


# ---------------------------
# Main Program
# ---------------------------

def main():
    amount = float(input("Enter base amount: ₹"))

    print("\nSelect Region")
    print("1. India")
    print("2. USA")
    print("3. Dubai")

    choice = input("Enter choice: ")

    if choice == "1":
        generate_bill(amount, india_tax)
    elif choice == "2":
        generate_bill(amount, usa_tax)
    elif choice == "3":
        generate_bill(amount, dubai_tax)
    else:
        print("❌ Invalid choice!")


# Run program
main()