# Day 1: Variables and Data types
# Customer and product storage foundation

product_name = "Dell i7 WIN11 Laptop"    # string
price = 21000.15                         # float
stock = 56                               # int  
is_available = True                      # boolean

# List of products (inventory)
products = ["Wireless Mouse", "Keyboard", "Monitor", "Mouse Pad", "JBL Speaker"]

# Dictionary of customer info
customer = {
    "first_name": "John",
    "last_name": "Doe",
    "customer_number": "10897745",
    "mobile_number": "086 3366 180",
    "email": "john.doe83@gmail.com",
    "adress_line": "10 Beryldene road, Kloof, KZN",
    "postal_code": "3630",
    "loyalty_points": "1256"    
}

print("==== Product Information ====")
print(f"Product: {product_name}")
print(f"Price: R{price}")
print(f"Stock: {stock}")
print(f"Available: {is_available}")
print(f"Products in shop: {products}")
print()
print(f"Customer: {customer["first_name"]} {customer["last_name"]} has {customer["loyalty_points"]} loyalty points currently available.")