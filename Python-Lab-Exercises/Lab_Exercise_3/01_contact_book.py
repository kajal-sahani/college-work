"""
Lab Exercise 3 - Program 1
Contact Book using Lists and Dictionaries
Student: Kajal
"""

contacts = {}   # Dictionary to store contacts: name -> phone

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    contacts[name] = phone
    print(f"✅ Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\n----- Contact List -----")
    for name, phone in contacts.items():
        print(f"{name:<20} : {phone}")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"Found: {name} → {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")


print("=" * 45)
print("           CONTACT BOOK")
print("=" * 45)

while True:
    print("\n1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("\nEnter choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice!")
