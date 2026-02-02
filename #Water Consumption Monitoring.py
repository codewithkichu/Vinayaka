#Water Consumption Monitoring

n = int(input("Enter number of households: "))

excess_count = 0

for i in range(1, n + 1):
    water = int(input(f"\nEnter daily water consumption of Household {i} (in litres): "))

    if water <= 200:
        print("Usage Category: Normal Usage")
    elif water <= 400:
        print("Usage Category: High Usage")
    else:
        print("Usage Category: Excess Usage")
        excess_count += 1

print("\n------------------------------")
print("Number of Excess Usage Households:", excess_count)