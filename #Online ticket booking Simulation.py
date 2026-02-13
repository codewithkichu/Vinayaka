#Online ticket booking Simulation
total_seats = 50

print("🎬 Welcome to Online Ticket Booking System")
print("Total Seats Available:", total_seats)

while total_seats > 0:
    try:
        user_input = input("\nEnter number of tickets to book (or type 'exit' to quit): ")

        # Exit condition
        if user_input.lower() == "exit":
            print("Thank you for visiting. 👋")
            break

        tickets = int(user_input)

        # Validation 1: Zero or negative booking
        if tickets <= 0:
            raise Exception("Number of tickets must be greater than zero.")

        # Validation 2: Booking more than available
        if tickets > total_seats:
            raise Exception("Not enough seats available.")

        # Booking success
        total_seats -= tickets
        print(f"✅ Booking successful! {tickets} ticket(s) booked.")
        print(f"🎟 Seats remaining: {total_seats}")

        # Check if seats are full
        if total_seats == 0:
            print("\n🚫 All seats are fully booked!")
            break

    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")

    except Exception as e:
        print("❌ Error:", e)

print("\n🎉 Booking system closed.")