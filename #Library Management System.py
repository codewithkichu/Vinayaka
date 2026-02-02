#Library Management System

library = {}   # Stores books and their availability

# Function to add books
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")

    if book_id in library:
        print("❌ Book already exists!")
    else:
        library[book_id] = {"title": title, "issued": False}
        print("✅ Book added successfully!")

# Function to issue book
def issue_book():
    book_id = input("Enter Book ID to issue: ")

    if book_id not in library:
        print("❌ Book not found!")
    elif library[book_id]["issued"]:
        print("❌ Book already issued!")
    else:
        library[book_id]["issued"] = True
        print("✅ Book issued successfully!")

# Function to return book
def return_book():
    book_id = input("Enter Book ID to return: ")

    if book_id not in library:
        print("❌ Book not found!")
    elif not library[book_id]["issued"]:
        print("❌ Book was not issued!")
    else:
        library[book_id]["issued"] = False
        print("✅ Book returned successfully!")

# Function to search book
def search_book():
    keyword = input("Enter book title or ID to search: ").lower()
    found = False

    for book_id, data in library.items():
        if keyword in book_id.lower() or keyword in data["title"].lower():
            status = "Issued" if data["issued"] else "Available"
            print("📖 Book ID:", book_id, "| Title:", data["title"], "| Status:", status)
            found = True

    if not found:
        print("❌ No matching book found!")

# Main program
def main():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            issue_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            search_book()
        elif choice == "5":
            print("📚 Thank you for using Library System!")
            break
        else:
            print("❌ Invalid choice!")

# Run program
main()