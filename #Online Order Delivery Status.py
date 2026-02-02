#Online Order Delivery Status

n = int(input("Enter number of orders: "))

delayed_count = 0

for i in range(1, n + 1):
    days = int(input(f"\nEnter delivery time for Order {i} (in days): "))

    if days <= 2:
        print("Delivery Status: Fast Delivery")
    elif days <= 5:
        print("Delivery Status: Normal Delivery")
    else:
        print("Delivery Status: Delayed Delivery")
        delayed_count += 1

print("\n------------------------------")
print("Number of Delayed Orders:", delayed_count)