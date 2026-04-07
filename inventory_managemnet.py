inventory = {}

LOW_STOCK_LIMIT = 5.0

def add_item():
    name = input("Enter item name: ").lower()
    qty = float(input("Enter quantity in kg: "))
    price = float(input("Enter price per kg: "))
    
    if name in inventory:
        inventory[name]["quantity"] += qty   # ✅ add stock instead of replace
        inventory[name]["price"] = price
        print("Item already exists → Stock updated")
    else:
        inventory[name] = {"quantity": qty, "price": price}
        print("Item added successfully")

def restock_item():
    name = input("Enter item name: ").lower()
    
    if name in inventory:
        qty = float(input("Enter quantity to add (kg): "))
        inventory[name]["quantity"] += qty
        print("Stock updated successfully")
    else:
        print("Item not found")

def update_price():
    name = input("Enter item name: ").lower()
    
    if name in inventory:
        price = float(input("Enter new price per kg: "))
        inventory[name]["price"] = price
        print("Price updated successfully")
    else:
        print("Item not found")

def sell_item():
    name = input("Enter item name: ").lower()
    
    if name in inventory:
        qty = float(input("Enter quantity to sell (kg): "))
        
        if qty <= inventory[name]["quantity"]:
            price = inventory[name]["price"]
            total = qty * price
            
            inventory[name]["quantity"] -= qty
            
            print("Total Bill:", total)
            print("Remaining stock:", inventory[name]["quantity"], "kg")
        else:
            print("Not enough stock")
    else:
        print("Item not found")

def display_inventory():
    if not inventory:
        print("Inventory is empty")
    else:
        print("\nItem\tQuantity(kg)\tPrice/kg\tStatus")
        for item in inventory:
            qty = inventory[item]["quantity"]
            
            status = "OK"
            if qty <= LOW_STOCK_LIMIT:
                status = "LOW STOCK ⚠️"
            
            print(f"{item.title()}\t{qty}\t\t{inventory[item]['price']}\t\t{status}")

def menu():
    while True:
        print("\n1. Add Item")
        print("2. Restock Item")
        print("3. Update Price")
        print("4. Sell Item")
        print("5. Display Inventory")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_item()
        elif choice == 2:
            restock_item()
        elif choice == 3:
            update_price()
        elif choice == 4:
            sell_item()
        elif choice == 5:
            display_inventory()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

menu()