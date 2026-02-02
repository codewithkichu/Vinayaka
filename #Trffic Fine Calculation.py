#Trffic Fine Calculation

n = int(input("Enter number of vehicles: "))

total_fine = 0

for i in range(1, n + 1):
    speed = int(input(f"\nEnter speed of Vehicle {i} (km/h): "))

    if speed <= 60:
        fine = 0
    elif speed <= 80:
        fine = 500
    else:
        fine = 1000

    print(f"Fine for Vehicle {i}: ₹{fine}")
    total_fine += fine

print("\n------------------------------")
print("Total Fine Collected: ₹", total_fine)