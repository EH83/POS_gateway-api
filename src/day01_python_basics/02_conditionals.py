# Day 1: If / Elif / Else Statements
 
# Stock check example
stock = 10
order_quantity = 10

if order_quantity > stock:
    print("Not enough stock available!")
elif order_quantity == stock:
    print("Order will empty stock!")
else: 
    print(f"Order approved! {order_quantity} units shipped.")

# Discount Logic
total = 450
if total > 1000:
    print("You get 15% off!")
elif total > 500:
    print("You get 10% off!")
else: print("No discount available this time")        