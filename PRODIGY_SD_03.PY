import json

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email):
        self.contacts[name] = {'phone': phone_number, 'email': email}
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

    def edit_contact(self, name, new_phone=None, new_email=None):
        if name in self.contacts:
            contact = self.contacts[name]
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            print(f"Contact '{name}' edited successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def save_contacts_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.contacts, file)
        print("Contacts saved successfully.")

    def load_contacts_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.contacts = json.load(file)
            print("Contacts loaded successfully.")
        except FileNotFoundError:
            print("No contacts file found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save Contacts to File")
        print("6. Load Contacts from File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_manager.add_contact(name, phone, email)
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            name = input("Enter contact name to edit: ")
            new_phone = input("Enter new phone number (leave blank to keep unchanged): ")
            new_email = input("Enter new email address (leave blank to keep unchanged): ")
            contact_manager.edit_contact(name, new_phone, new_email)
        elif choice == '4':
            name = input("Enter contact name to delete: ")
            contact_manager.delete_contact(name)
        elif choice == '5':
            filename = input("Enter filename to save contacts: ")
            contact_manager.save_contacts_to_file(filename)
        elif choice == '6':
            filename = input("Enter filename to load contacts from: ")
            contact_manager.load_contacts_from_file(filename)
        elif choice == '7':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
