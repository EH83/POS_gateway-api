# Day 1: Functions (reusable code)

def calculate_total(price, quantity):
    # calculate order total
    return price * quantity

def apply_discount(total, discount_percentage=10):
    # apply discount if total is high enough
    if total > 500:
        discount = total * (discount_percentage / 100)
        return total - discount
    return total

# testing the functions
order_total = calculate_total(505.99, 3)
final_price = apply_discount(order_total)

print(f"Order total before discount: R{order_total:.2f}")
print(f"Final price after discount: R{final_price:.2f}")