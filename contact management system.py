class ContactManager:
    def __init__(self):
        self.contacts = {}
        self.groups = {}

    def add_contact(self, name, phone, email="", address="", group=None):
        contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address,
            'groups': set()
        }
        
        self.contacts[name] = contact
        if group:
            self.add_to_group(name, group)
        print(f"Added contact: {name}")

    def add_to_group(self, name, group_name):
        if name not in self.contacts:
            print(f"Contact {name} not found!")
            return
            
        if group_name not in self.groups:
            self.groups[group_name] = set()
            
        self.groups[group_name].add(name)
        self.contacts[name]['groups'].add(group_name)
        print(f"Added {name} to group: {group_name}")

    def search_contacts(self, term):
        results = []
        term = term.lower()
        
        for contact in self.contacts.values():
            if (term in contact['name'].lower() or
                term in contact['phone'] or
                term in contact['email'].lower()):
                results.append(contact)
                
        return results

    def display_contact(self, contact):
        print("\n" + "=" * 40)
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        if contact['email']:
            print(f"Email: {contact['email']}")
        if contact['address']:
            print(f"Address: {contact['address']}")
        if contact['groups']:
            print(f"Groups: {', '.join(contact['groups'])}")
        print("=" * 40)

    def list_group(self, group_name):
        if group_name not in self.groups:
            print(f"Group {group_name} not found!")
            return
            
        print(f"\nContacts in group '{group_name}':")
        for name in self.groups[group_name]:
            self.display_contact(self.contacts[name])

    def delete_contact(self, name):
        if name not in self.contacts:
            print(f"Contact {name} not found!")
            return
            
        # Remove from all groups
        for group in self.groups.values():
            group.discard(name)
            
        del self.contacts[name]
        print(f"Deleted contact: {name}")

    def show_menu(self):
        while True:
            print("\nContact Manager Menu:")
            print("1. Add Contact")
            print("2. Search Contacts")
            print("3. List Group")
            print("4. Add Contact to Group")
            print("5. Delete Contact")
            print("6. Exit")
            
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == "1":
                name = input("Enter name: ").strip()
                phone = input("Enter phone: ").strip()
                email = input("Enter email (optional): ").strip()
                address = input("Enter address (optional): ").strip()
                group = input("Enter group (optional): ").strip()
                self.add_contact(name, phone, email, address, group)
                
            elif choice == "2":
                term = input("Enter search term: ").strip()
                results = self.search_contacts(term)
                if results:
                    print(f"\nFound {len(results)} contacts:")
                    for contact in results:
                        self.display_contact(contact)
                else:
                    print("No contacts found!")
                    
            elif choice == "3":
                group = input("Enter group name: ").strip()
                self.list_group(group)
                
            elif choice == "4":
                name = input("Enter contact name: ").strip()
                group = input("Enter group name: ").strip()
                self.add_to_group(name, group)
                
            elif choice == "5":
                name = input("Enter contact name to delete: ").strip()
                self.delete_contact(name)
                
            elif choice == "6":
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice! Please try again.")

def main():
    manager = ContactManager()
    
    # Add some sample contacts
    manager.add_contact("John Smith", "555-0123", "john@email.com", "123 Main St", "Friends")
    manager.add_contact("Jane Doe", "555-0456", "jane@email.com", "456 Oak Ave", "Family")
    manager.add_contact("Bob Wilson", "555-0789", "bob@email.com", "789 Pine St", "Work")
    
    # Start the menu
    manager.show_menu()

if __name__ == "__main__":
    main()