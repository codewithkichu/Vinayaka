#Electricity Bill Calculation System

units = 0
bill_amount = 0

def input_units():
    global units
    units = int(input("Enter units consumed: "))
    if units < 0:
        print("❌ Invalid units!")
        input_units()

def calculate_bill():
    global bill_amount

    if units <= 100:
        bill_amount = units * 2
    elif units <= 200:
        bill_amount = (100 * 2) + (units - 100) * 3
    else:
        bill_amount = (100 * 2) + (100 * 3) + (units - 200) * 5

def generate_bill_summary():
    print("\n⚡ Electricity Bill Summary")
    print("---------------------------")
    print("Units Consumed:", units)
    print("Total Bill Amount: ₹", bill_amount)

def main():
    input_units()
    calculate_bill()
    generate_bill_summary()

# Run program
main()