# Day 1: For loops and While loops

#For loop - print inventory
products = ["TV", "Speaker", "Kettle", "Toaster", "Microwave", "Fridge"]

print("------ Shop Inventory ------")
for product in products:
    print(f" .{product}")

#While loop - stock counter
stock = 5
while stock > 0:
    print(f"Stock remaining: {stock} ")
    stock -= 1
print("Out of stock!")        