# store all inventory items
inventory = []
# main program loop
while True:
    print("\n=== Inventory Manager ===")
    print("1. Add new item")
    print("2. Update stock quantity")
    print("3. Search for item")
    print("4. View all items")
    print("5. Generate low stock report")
    print("6. Exit")
    choice = input("Enter choice: ")
    #add new item with duplicate check
    if choice == "1":   
        item_name = input("Enter item name: ").lower()
        duplicate = False
        #check if item exists
        for item in inventory:
            if item["name"] == item_name:
                duplicate = True
                break  
        if duplicate:
            print("Item already exists!")        
        else:
            item_price = float(input("Enter price: "))
            item_quantity = int(input("Enter quantity: "))
            reorder_level = int(input("Enter reorder level: "))
            #create items dict
            items = {
            "name": item_name,
            "price": item_price,
            "quantity": item_quantity,
            "reorder": reorder_level
            }
            #append items dict to list
            inventory.append(items)
            print("Item added successfully!")
    # update stock quantity
    elif choice == "2":
        update_name = input("Enter item name: ").lower()
        found = False
        for item in inventory:
            if item["name"] == update_name:
                change = int(input("Enter quantity change (+/-): "))
                item["quantity"] += change
                print(f"Updated! New quantity: {item['quantity']}")
                found = True
                break
        if not found:
            print("Item not found!")     
    #search for specific item
    elif choice == "3":
        search_name = input("Enter item name to search: ").lower()
        found = False
        for item in inventory:
            if item["name"] == search_name:
                print("\n--- Item Details ---")
                print(f"Name: {item['name']}")
                print(f"Price: R{item['price']:.2f}")
                print(f"Quantity: {item['quantity']}")
                print(f"Reorder Level: {item['reorder']}")
                found = True
                break  
        if not found:             
            print("Item not found!")
    #view all items
    elif choice == "4":
        for item in inventory:
            print("\n--- View all Items ---")
            print(f"Name: {item['name']}")
            print(f"Price: R{item['price']:.2f}")
            print(f"Quantity: {item['quantity']}")
            print(f"Reorder Level: {item['reorder']}")  
            print()     
    #generate low stock report     
    elif choice =="5":
        print("\n--- Low Stock Report ---")
        low_stock_items = []
        #find items at or below reorder level
        for item in inventory:
            if item["quantity"] <= item["reorder"]:
                low_stock_items.append(item)

        if len(low_stock_items) == 0:
            print("All items sufficiently stocked")
        else:
            for item in low_stock_items:
                print(f"{item['name']}: {item['quantity']} in stock (reorder at {item['reorder']})") 
    #exit program
    elif choice == "6":
        print("Goodbye!")
        break 

          






