import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('inventory.db')
c = conn.cursor()

# Create the inventory table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )''')

# Function to add an item
def add_item(name, quantity, price):
    c.execute('INSERT INTO inventory (name, quantity, price) VALUES (?, ?, ?)', (name, quantity, price))
    conn.commit()
    print(f'Added {name} to the inventory.')

# Function to update an item
def update_item(item_id, name, quantity, price):
    c.execute('UPDATE inventory SET name = ?, quantity = ?, price = ? WHERE id = ?', (name, quantity, price, item_id))
    conn.commit()
    print(f'Updated item with ID {item_id}.')

# Function to delete an item
def delete_item(item_id):
    c.execute('DELETE FROM inventory WHERE id = ?', (item_id,))
    conn.commit()
    print(f'Deleted item with ID {item_id}.')

# Function to view all items
def view_items():
    c.execute('SELECT * FROM inventory')
    items = c.fetchall()
    for item in items:
        print(item)

# Example usage
add_item('Laptop', 10, 999.99)
add_item('Smartphone', 20, 499.99)
view_items()
update_item(1, 'Laptop', 8, 949.99)
delete_item(2)
view_items()

# Close the database connection
conn.close()
