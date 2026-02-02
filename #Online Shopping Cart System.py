#Online Shopping Cart System

cart = []   # Stores item prices

def add_item():
    price = float(input("Enter item price: ₹"))
    
    if price > 0:
        cart.append(price)
        print("✅ Item added to cart!")
    else:
        print("Invalid price!")

def remove_item():
    if len(cart) == 0:
        print("❌ Cart is empty!")
    else:
        price = float(input("Enter item price to remove: ₹"))
        if price in cart:
            cart.remove(price)
            print("✅ Item removed successfully!")
        else:
            print("❌ Item not found in cart!")

def calculate_total():
    total = sum(cart)
    print("🧾 Total Bill: ₹", total)
    return total

def apply_discount():
    total = calculate_total()
    discount = float(input("Enter discount percentage: "))

    if 0 <= discount <= 100:
        discount_amount = total * discount / 100
        final_amount = total - discount_amount
        print("🎉 Discount Applied!")
        print("💰 Final Amount: ₹", final_amount)
    else:
        print("❌ Invalid discount percentage!")

def main():
    while True:
        print("\n--- Online Shopping Cart ---")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Calculate Total Bill")
        print("4. Apply Discount")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            apply_discount()
        elif choice == "5":
            print("Thank you for shopping 🛍️")
            break
        else:
            print("❌ Invalid choice!")

# Run the program
main()