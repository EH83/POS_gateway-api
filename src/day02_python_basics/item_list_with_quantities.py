#empty list
inventory = []
#priming read statement
item_name = (input("What item is this?: ").strip().lower())

while item_name != "done":
    item_price = float((input("What is the item's price?: ").strip()))
    item_quantity = int((input("How may are there?: ").strip()))
    #build items dict
    items = {
        "name": item_name,
        "price": item_price,
        "quantity": item_quantity
    }
    #add items to inventory 
    inventory.append(items)
    item_name = (input("What item is this?: ").strip().lower()) 

tax_rate = float(input("What is the tax rate for these items?: ")) 
subtotal = 0 
#inventory loop & print receipt
for item in inventory:  
    item_total = item["price"] * item["quantity"]
    subtotal += item_total
    print(f"{item['name']} (x{item['quantity']}): R{item_total:.2f}") 
#tax & grand total calculations    
tax_due = subtotal * (tax_rate / 100)
total = subtotal + tax_due
#final print statements
print(f"Subtotal: R{subtotal:.2f}")
print(f"Tax: R{tax_due:.2f}")
print(f"Grand Total: R{total:.2f}")