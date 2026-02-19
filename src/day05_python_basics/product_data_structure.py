#calc total inventory product value
def total_value(product_price, product_stock):
    return product_price * product_stock
#test case 1: Valid product
product_name = "Samsung 75 Smart TV"
product_price = float(12999.99)
product_stock = int(25)
#validate product data & output
if product_price > 0 and product_stock >= 0 and product_name != "":
    print("Valid Products Created!")
    print(f"Product: {product_name}")
    print(f"Price: R{product_price:.2f}")
    print(f"Stock: {product_stock} units")
    print(f"Total Inventory Value: {total_value(product_price, product_stock):.2f}")
else:
    print("Error no products created!")

print()
#test case 2: invalid price
product_name = "Test"
product_price = float(-100.65)
product_stock = int(10)

if product_price > 0 and product_stock >= 0 and product_name != "":
    print("Valid Products Created!")
    print(f"Product: {product_name}")
    print(f"Price: R{product_price:.2f}")
    print(f"Stock: {product_stock} units")
    print(f"Total Inventory Value: {total_value(product_price, product_stock):.2f}")
else:
    print("Error no products created!")

print()
#test case 3: invalid name
product_name = ""
product_price = float(500)
product_stock = int(5)

if product_price > 0 and product_stock >= 0 and product_name != "":
    print("Valid Products Created!")
    print(f"Product: {product_name}")
    print(f"Price: R{product_price:.2f}")
    print(f"Stock: {product_stock} units")
    print(f"Total Inventory Value: {total_value(product_price, product_stock):.2f}")
else:
    print("Error no products created!")