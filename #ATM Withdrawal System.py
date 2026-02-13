#ATM Withdrawal System

balance = 10000  # Initial balance

print("🏧 Welcome to ATM")
print("Your current balance is ₹", balance)

while True:
    try:
        user_input = input("\nEnter withdrawal amount (or type 'exit' to quit): ")

        # Exit condition
        if user_input.lower() == "exit":
            print("Thank you for using ATM. Goodbye! 👋")
            break

        # Convert input to integer
        amount = int(user_input)

        # Check for negative or zero amount
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        # Check for insufficient balance
        if amount > balance:
            raise ValueError("Insufficient balance.")

        # Deduct amount
        balance -= amount
        print(f"✅ Withdrawal successful! ₹{amount} withdrawn.")
        print(f"💰 Remaining balance: ₹{balance}")

    except ValueError as e:
        print("❌ Error:", e)

    except Exception:
        print("❌ Invalid input! Please enter a valid number.")