contacts = []  
def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    if name == "" or phone == "":
        print("Name and phone number are required.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully.")
    
def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\n--- Saved Contacts ---")
    for index, contact in enumerate(contacts, start=1):
        print(f"\nContact {index}")
        print(f"Name   : {contact['name']}")
        print(f"Phone  : {contact['phone']}")
        print(f"Email  : {contact['email']}")
        print(f"Address: {contact['address']}")

def search_contact():
    if not contacts:
        print("No contacts available to search.")
        return

    search_term = input("Enter name or phone number to search: ").strip().lower()

    found = False
    for contact in contacts:
        if search_term == contact["phone"] or search_term in contact["name"].lower():
            print("\n--- Contact Found ---")
            print(f"Name   : {contact['name']}")
            print(f"Phone  : {contact['phone']}")
            print(f"Email  : {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break

    if not found:
        print("Contact not found.")
    
def update_contact():
    
    pass
def delete_contact():
    
    pass
def main_menu():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()