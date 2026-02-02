#Simple Banking Application

balance = 0   # Global balance

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    
    if amount > 0:
        balance += amount
        print("✅ Deposit successful!")
    else:
        print("❌ Invalid amount!")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))
    
    if amount <= 0:
        print("❌ Invalid amount!")
    elif amount > balance:
        print("❌ Insufficient balance!")
    else:
        balance -= amount
        print("✅ Withdrawal successful!")

def check_balance():
    print("💰 Current Balance: ₹", balance)

def main():
    while True:
        print("\n--- Simple Banking Application ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            check_balance()
        elif choice == "4":
            print("Thank you for using the bank app 🙏")
            break
        else:
            print("❌ Invalid choice!")

# Run program
main()