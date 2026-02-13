#Student mark file processor
file_name = "students.txt"

valid_count = 0
invalid_count = 0
total_marks = 0

try:
    with open(file_name, "r") as file:
        lines = file.readlines()

        # Check for empty file
        if len(lines) == 0:
            raise ValueError("File is empty.")

        print("📄 Student Records:\n")

        for line in lines:
            try:
                line = line.strip()

                # Skip empty lines
                if not line:
                    continue

                parts = line.split(",")

                # Check file format
                if len(parts) != 2:
                    raise ValueError("Incorrect file format")

                name = parts[0].strip()
                marks = parts[1].strip()

                # Convert marks to integer
                marks = int(marks)

                if marks < 0:
                    raise ValueError("Marks cannot be negative")

                print(f"Name: {name} | Marks: {marks}")

                total_marks += marks
                valid_count += 1

            except ValueError:
                print(f"⚠ Invalid record skipped → {line}")
                invalid_count += 1

        # Calculate average
        if valid_count > 0:
            average = total_marks / valid_count
            print("\n📊 Average Marks:", average)
        else:
            print("\nNo valid records found.")

        print("\n📈 Summary:")
        print("Valid records:", valid_count)
        print("Invalid records:", invalid_count)

except FileNotFoundError:
    print("❌ Error: File not found.")

except ValueError as e:
    print("❌ Error:", e)

except Exception as e:
    print("❌ Unexpected error:", e)