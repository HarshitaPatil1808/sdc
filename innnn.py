# Inventory Management System

# Inventory data structure
inventory = {}

# Function to display menu
def display_menu():
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit")

# Function to add an item
def add_item():
    item_id = input("Enter item ID: ")
    if item_id in inventory:
        print("Item already exists!")
    else:
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory[item_id] = {"name": name, "quantity": quantity, "price": price}
        print("Item added successfully!")

# Function to view inventory
def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nID\tName\t\tQuantity\tPrice")
        for item_id, details in inventory.items():
            print(f"{item_id}\t{details['name']}\t{details['quantity']}\t{details['price']}")

# Function to update an item
def update_item():
    item_id = input("Enter item ID to update: ")
    if item_id in inventory:
        print("What would you like to update?")
        print("1. Name")
        print("2. Quantity")
        print("3. Price")
        choice = int(input("Enter choice: "))
        if choice == 1:
            inventory[item_id]['name'] = input("Enter new name: ")
        elif choice == 2:
            inventory[item_id]['quantity'] = int(input("Enter new quantity: "))
        elif choice == 3:
            inventory[item_id]['price'] = float(input("Enter new price: "))
        else:
            print("Invalid choice.")
        print("Item updated successfully!")
    else:
        print("Item not found.")

# Function to delete an item
def delete_item():
    item_id = input("Enter item ID to delete: ")
    if item_id in inventory:
        del inventory[item_id]
        print("Item deleted successfully!")
    else:
        print("Item not found.")

# Main program
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        add_item()
    elif choice == '2':
        view_inventory()
    elif choice == '3':
        update_item()
    elif choice == '4':
        delete_item()
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
