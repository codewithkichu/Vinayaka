#Menu-Driven Utility Application

# -----------------------
# Calculator Functions
# -----------------------

def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose operation: ")

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        if b != 0:
            print("Result:", a / b)
        else:
            print("❌ Cannot divide by zero!")
    else:
        print("❌ Invalid choice!")

# -----------------------
# String Utility
# -----------------------

def string_operations():
    text = input("Enter a string: ")

    print("1. Uppercase")
    print("2. Lowercase")
    print("3. Reverse")
    print("4. Length")

    choice = input("Choose option: ")

    if choice == "1":
        print("Result:", text.upper())
    elif choice == "2":
        print("Result:", text.lower())
    elif choice == "3":
        print("Result:", text[::-1])
    elif choice == "4":
        print("Length:", len(text))
    else:
        print("❌ Invalid choice!")

# -----------------------
# Number Utility
# -----------------------

def number_utilities():
    num = int(input("Enter a number: "))

    print("1. Check Even/Odd")
    print("2. Factorial")
    print("3. Prime Check")

    choice = input("Choose option: ")

    if choice == "1":
        print("Even" if num % 2 == 0 else "Odd")

    elif choice == "2":
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        print("Factorial:", fact)

    elif choice == "3":
        if num < 2:
            print("Not Prime")
        else:
            prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    prime = False
                    break
            print("Prime" if prime else "Not Prime")

    else:
        print("❌ Invalid choice!")

# -----------------------
# Main Menu
# -----------------------

def main():
    while True:
        print("\n--- Menu Driven Utility App ---")
        print("1. Calculator")
        print("2. String Operations")
        print("3. Number Utilities")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            string_operations()
        elif choice == "3":
            number_utilities()
        elif choice == "4":
            print("👋 Exiting Application")
            break
        else:
            print("❌ Invalid choice!")

# Run program
main()