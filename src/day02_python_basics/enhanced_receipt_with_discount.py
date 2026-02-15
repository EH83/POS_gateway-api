inventory = []
item_name = input("What is the item name?: ").lower()
while item_name != "done":
    item_price = float(input("What is the item price?: "))
    item_quantity = int(input("Quantity?: "))
    item_discount = float(input("What is the item discount? :"))
    items = {
        "name" : item_name,
        "price" : item_price,
        "quantity" : item_quantity,
        "discount" : item_discount
    }
    inventory.append(items)
    item_name = input("What is the item name?: ").lower()

tax_rate = float(input("What is the tax rate for these items?: ")) 
subtotal = 0 
#Receipt header
print("\n---- Receipt ----")
#fix these outputs
for item in inventory:
    discount_amount = item["price"] * (item["discount"] / 100)
    final_price = item["price"] - discount_amount
    item_total = final_price * item["quantity"]
    subtotal += item_total
    #if discount present print statements
    if item["discount"] > 0:
        print(f"\n{item['name']} (x{item['quantity']}):")
        print(f"  Original: R{item['price']:.2f}")
        print(f"  Discount ({item['discount']}%): -R{discount_amount:.2f}")
        print(f"  Price: R{final_price:.2f}")
        print(f"  Total: R{item_total:.2f}")
    #if discount not present print statements
    else: 
        print(f"\n{item['name']} (x{item['quantity']}):")
        print(f"  Price: R{item['price']:.2f}")
        print(f"  Total: R{item_total:.2f}")
#final totals print
tax_due = subtotal * (tax_rate / 100)
total = subtotal + tax_due
print(f"\nSubtotal: R{subtotal:.2f}")
print(f"Tax ({tax_rate}%): R{tax_due:.2f}")
print(f"Grand Total: R{total:.2f}")










