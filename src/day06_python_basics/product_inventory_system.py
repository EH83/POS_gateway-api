#helper function to calc total inventory for a product
def total_value(price, stock):
    return price * stock
#initialize empty list to store product dictionaries
inventory = []
#dict products specified
product1 = {
    "name" : "Laptop",
    "price" : 12999.99,
    "stock" : 25
}

product2 = {
    "name" : "Mouse",
    "price" : 499.99,
    "stock" : 50
}    

product3 = {
    "name" : "Monitor",
    "price" : 4500.50,
    "stock" : 23
}

product4 = {
    "name" : "Keyboard",
    "price": 1200.45,
    "stock" : 34
}

product5 = {
    "name" : "Headphone",
    "price" : 2330.00,
    "stock" : 78
}

#add all products to inventory list
inventory.append(product1)
inventory.append(product2)
inventory.append(product3)
inventory.append(product4)
inventory.append(product5)
#loop through inventory and display product details
print("\n---Product Inventory---")
print()
#initialize counter for product numbering  
item_counter = 1
for product in inventory:
    print(f"Product: {item_counter}")
    print(f"Product Name: {product["name"]}")
    print (f"Product Price: R{product["price"]:.2f}")
    print(f"Product Stock: {product["stock"]} units")
    value = total_value(product["price"], product["stock"])
    print(f"Value: R{value:.2f}")
    print()
    #increment counter for next product
    item_counter += 1
#initialize accumulators for stat calcs
total_inventory_value = 0
total_price_sum = 0
total_stock_items = 0
highest_value = 0
highest_value_product_name = ""
#accumulators loop for stats
for product in inventory:
    value = total_value(product["price"], product["stock"])
    total_inventory_value = total_inventory_value + value
    total_price_sum = total_price_sum + product["price"]
    total_stock_items = total_stock_items + product["stock"]
    #determine if current prodcust is highest
    if value > highest_value:
        highest_value = value
        highest_value_product_name = product["name"]
#calc average products price
average_price = total_price_sum / len(inventory) 
#display final stats
print("\n=== Inventory Summary ===")
print(f"Total Products: {len(inventory)}")
print(f"Total Inventory Value: R{total_inventory_value:.2f}")
print(f"Average Product Price: R{average_price:.2f}")
print(f"Total Stock Items: {total_stock_items}")
print(f"Highest Value Product: {highest_value_product_name} (R{highest_value:.2f})")


    







