#item price input
item_price = float(input("Please enter item price: "))
#running subtotal
subtotal = 0
#subtotal loop & price input
while item_price != 0:
    subtotal += item_price 
    item_price = float(input("Please enter item price: "))  
#condition statement & tax & price calcs   
    if item_price == 0:
        tax_rate = float(input("What is the tax rate for these items?: "))
        tax_due = subtotal * (tax_rate / 100)
        total = subtotal + tax_due
        #exit clause 
        break
#final print totals stataments    
print(f"Subtotal: R{subtotal:.2f}")
print(f"Total tax due: R{tax_due:.2f}")
print(f"Total amount due: R{total :.2f}")

