#item price & tax inputs
item_price = float(input("Please input item price: "))
tax_rate = float(input("Please input tax rate: "))
#tax & final price calcs
tax_amount = item_price * (tax_rate / 100) 
final_price = item_price + tax_amount
#final price print
print(f"The total item price is {final_price:.2f}")