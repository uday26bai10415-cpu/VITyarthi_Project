users_db = {}


def create_account():
    """Register a new user with a unique username and password."""
    print("\nCreate An Account")
    new_user = input("Username: ").strip()

    if not new_user:
        print("Username cannot be empty.")
        return

    if new_user in users_db:
        print("User already exists.")
        return

    new_pass = input("Password: ").strip()
    if not new_pass:
        print("Password cannot be empty.")
        return

    users_db[new_user] = {"password": new_pass, "docs": []}
    print("Account created successfully.")


def login():
    """Authenticate a user. Returns the username on success, else None."""
    print("\nLogin")
    entered_user = input("Username: ").strip()
    entered_pass = input("Password: ").strip()

    if entered_user in users_db and users_db[entered_user]["password"] == entered_pass:
        print("Login successful.")
        return entered_user

    print("Wrong Credentials.")
    return None


def upload_doc(username):
    """Add a new document (name + type) to the logged-in user's profile."""
    print("\nUpload Document")
    file_name = input("Document name: ").strip()
    file_type = input("Type (PDF/Image/etc): ").strip()

    if not file_name or not file_type:
        print("Document name and type cannot be empty.")
        return

    new_doc = {"name": file_name, "type": file_type}
    users_db[username]["docs"].append(new_doc)
    print("Document Uploaded.")


def view_docs(username):
    """Display every document belonging to the logged-in user."""
    print("\nYour Documents:")
    all_docs = users_db[username]["docs"]

    if not all_docs:
        print("No documents found.")
        return

    for idx, doc in enumerate(all_docs, start=1):
        print(f"{idx}. {doc['name']} ({doc['type']})")


def search_doc(username):
    """Search the logged-in user's documents by a case-insensitive keyword."""
    print("\nSearch Documents")
    keyword = input("Keyword: ").strip().lower()

    if not keyword:
        print("Please enter a keyword to search.")
        return

    found_any = False
    for doc in users_db[username]["docs"]:
        if keyword in doc["name"].lower():
            print(f"- {doc['name']} ({doc['type']})")
            found_any = True

    if not found_any:
        print("No matching documents found.")


def delete_doc(username):
    """Delete a document chosen by its displayed list number."""
    print("\nDelete Document")
    user_docs = users_db[username]["docs"]

    if not user_docs:
        print("No documents to delete.")
        return

    view_docs(username)

    try:
        choice = int(input("Enter document number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if 1 <= choice <= len(user_docs):
        removed_doc = user_docs.pop(choice - 1)
        print(f"'{removed_doc['name']}' deleted successfully.")
    else:
        print("Invalid document number.")


def user_menu(username):
    """Dashboard shown to a logged-in user, looping until they log out."""
    while True:
        print(f"\n--- Welcome, {username.upper()} ---")
        print("1. Upload Document")
        print("2. View Documents")
        print("3. Search Document")
        print("4. Delete Document")
        print("5. Logout")

        choice = input("Choice: ").strip()

        if choice == "1":
            upload_doc(username)
        elif choice == "2":
            view_docs(username)
        elif choice == "3":
            search_doc(username)
        elif choice == "4":
            delete_doc(username)
        elif choice == "5":
            print("Logged out.")
            break
        else:
            print("Invalid choice. Try again.")


def main():
    """Main entry point: account creation / login menu."""
    while True:
        print("\n===== Mini DigiLocker =====")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Choice: ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            active_user = login()
            if active_user:
                user_menu(active_user)
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
