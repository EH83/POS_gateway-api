#calculate totals & tax
def calculate_transaction(price, qty, tax_rate):
    subtotal = price * qty
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount
    return subtotal, tax_amount, total

#transaction data
customer_name = "John Doe"
item_purchased = "Samsung Laptop"
item_price = float(23123.99)
quantity = int(1)
tax_rate = float(0.15)
customer_payment = float(27000.00)

#calc transaction values
subtotal, tax_amount, total = calculate_transaction(item_price, quantity, tax_rate)

if item_price > 0 and quantity > 0 :
    if customer_payment >= total:
    #display outputs
        print("\n===Transaction Receipt===")
        print(f"Customer: {customer_name}")
        print(f"Item: {item_purchased}")
        print(f"Price: {item_price:.2f}")
        print("---------------------------")
        print(f"Subtotal: {subtotal:.2f}")
        print("---------------------------")
        print(f"Tax: {tax_amount:.2f}")
        print("---------------------------")
        print()
        print(f"Total: {total:.2f}")
        print("===Thank You!===")

        change = customer_payment - total
        print(f"Payment: R{customer_payment:.2f}")
        print(f"Change: R{change:.2f}")
    else:
        shortage = total - customer_payment
        print("\n TRANSACTION DECLINED")
        print(f"Total Due: R{total:.2f}")
        print(f"Payment: R{customer_payment:.2f}")
        print(f"Short: R{shortage:.2f}")
else:
    print("\n ERROR: Invalid price or quantity!")