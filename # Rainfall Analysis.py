# Rainfall Analysis

n = int(input("Enter number of days: "))

heavy_count = 0

for i in range(1, n + 1):
    rainfall = float(input(f"\nEnter rainfall for Day {i} (in mm): "))

    if rainfall < 10:
        print("Rainfall Status: Low")
    elif rainfall <= 50:
        print("Rainfall Status: Moderate")
    else:
        print("Rainfall Status: Heavy")
        heavy_count += 1

print("\n------------------------------")
print("Number of Heavy Rainfall Days:", heavy_count)