#Moblie Data Usage Monitoring

n = int(input("Enter number of users: "))

extra_count = 0

for i in range(1, n + 1):
    data = float(input(f"\nEnter data usage of User {i} (in GB): "))

    if data <= 1:
        print("Usage Status: Normal")
    elif data <= 2:
        print("Usage Status: Warning")
    else:
        print("Usage Status: Extra Charges")
        extra_count += 1

print("\n------------------------------")
print("Users with Extra Charges:", extra_count)