#HELPER FUNCTIONS

def get_tier(total_spent):
    """Returns tier based on spending"""
    if total_spent >= 10000:
        return "Platinum"
    elif total_spent >= 5000:
        return "Gold"
    elif total_spent >= 1000:
        return "Silver"
    else:
        return "Bronze"

def get_multiplier(total_spent):
    """Returns points multiplier"""
    if total_spent >= 10000:
        return 3
    elif total_spent >= 5000:
        return 2
    elif total_spent >= 1000:
        return 1.5
    else:
        return 1

def get_discount_percentage(total_spent):
    """Returns discount %"""
    if total_spent >= 10000:
        return 15
    elif total_spent >= 5000:
        return 10
    elif total_spent >= 1000:
        return 5
    else:
        return 0

def get_total_spent(customer):
    """Returns customer's total spending for sorting"""
    return customer["total_spent"]

# Main data structure - list of customer dictionaries
# Each customer: {name, customer_id, email, loyalty_points, total_spent, purchases[]}
customers = []

# Main menu loop
while True:
    print("\n=== Customer Sales & Loyalty Program ===")
    print("1. Register new customer")
    print("2. Record purchase")
    print("3. View customer profile")
    print("4. Apply loyalty discount to purchase")
    print("5. View top customers")
    print("6. Generate sales report")
    print("7. Exit")
    choice = input("Enter choice: ")

    #CHOICE 1: Register new customer
    if choice == "1":
        cust_number = input("Enter customer number: ").strip().upper()
        
        duplicate = False
        for customer in customers:
            if customer["customer_id"] == cust_number:
                duplicate = True
                break
        
        if duplicate:
            print("Customer already exists!")    
        else:
            cust_name = input("What is the customer name?: ").lower()
            cust_mail = input("What is customer email address?: ").lower().strip()    

            details = {
                "name" : cust_name,
                "customer_id": cust_number,
                "email" : cust_mail,
                "loyalty_points": 50,      # Signup bonus
                "total_spent": 0.0,
                "purchases": []
            }
            customers.append(details)
            print("Customer registered successfully!")
            print("50 bonus points awarded!")   

    #CHOICE 2: Record purchase
    elif choice == "2":
        # Find customer using "found flag" pattern
        search_id = input("Enter customer number to search: ").strip().upper()
        found = False
        
        for customer in customers:
            if customer["customer_id"] == search_id:
                found = True

                purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
                purchase_amount = float(input("Enter purchase amount: ").strip().replace(" ", ""))
                num_items = int(input("Enter number of items: ").strip().replace(" ", ""))

                purchase = {
                    "date" : purchase_date,
                    "amount" : purchase_amount,
                    "items" : num_items
                }

                customer["purchases"].append(purchase)
                customer["total_spent"] += purchase_amount

                # Points formula: (amount/100) * 10 * multiplier
                multiplier = get_multiplier(customer["total_spent"])
                points_earned = (purchase_amount / 100) * 10 * multiplier
                customer["loyalty_points"] += points_earned

                print(f"\nPurchase recorded!")
                print(f"Points earned: {points_earned:.0f} ({get_tier(customer['total_spent'])} tier: {multiplier}x multiplier)")
                print(f"Total points: {customer['loyalty_points']:.0f}")
                print(f"Current tier: {get_tier(customer['total_spent'])}")
                break

        if not found:
            print("Customer not found!")    

    #CHOICE 3: View customer profile
    elif choice == "3":
        # Find customer using "found flag" pattern
        search_id = input("Enter customer number to search: ").strip().upper()
        found = False
        
        for customer in customers:
            if customer["customer_id"] == search_id:
                print("\n--- Customer Profile ---")
                print(f"Name: {customer['name']}")
                print(f"Number: {customer['customer_id']}")
                print(f"Email: {customer['email']}")
                print(f"Loyalty Tier: {get_tier(customer['total_spent'])}")
                print(f"Loyalty Points: {customer['loyalty_points']:.0f}")
                print(f"Total Spent: R{customer['total_spent']:.2f}")
                print(f"Number of Purchases: {len(customer['purchases'])}")

                if len(customer['purchases']) > 0:
                    print("\nPurchase History:")
                    for i, purchase in enumerate(customer['purchases'], 1):
                        print(f" {i}. {purchase['date']}: R{purchase['amount']:.2f} ({purchase['items']} items)")

                print(f"\nAvailable Discount: {get_discount_percentage(customer['total_spent'])}%")        
                found = True
                break

        if not found:             
            print("Customer not found!")

    #CHOICE 4: Apply discount
    elif choice == "4":
        # Find customer using "found flag" pattern
        search_id = input("Enter customer number to search: ").strip().upper()
        found = False
        
        for customer in customers:
            if customer["customer_id"] == search_id:
                found = True

                purchase_amount = float(input("Enter purchase amount: ").strip().replace(" ", ""))

                discount_percent = get_discount_percentage(customer["total_spent"])
                tier_discount = purchase_amount * (discount_percent / 100)

                print(f"Tier discount: {discount_percent}% (R{tier_discount:.2f})")
                print(f"Available points: {customer['loyalty_points']:.0f}")
                points_to_use = int(input("How many points would you like to use? ").strip().replace(" ", ""))

                if points_to_use > customer["loyalty_points"]:
                    print("Not enough points! Using 0 points.")
                    points_to_use = 0

                points_discount = points_to_use / 10
                total_discount = tier_discount + points_discount
                max_discount = purchase_amount * 0.5

                if total_discount > max_discount:
                    total_discount = max_discount
                    print("Discount capped at 50%")

                final_amount = purchase_amount - total_discount

                print(f"\n--- Purchase Breakdown ---")
                print(f"Original: R{purchase_amount:.2f}")
                print(f"Discount: R{total_discount:.2f}")
                print(f"Final: R{final_amount:.2f}")

                customer["loyalty_points"] -= points_to_use

                purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
                num_items = int(input("Enter the number of items: ").strip().replace(" ", ""))

                purchase = {
                    "date" : purchase_date,
                    "amount" : final_amount,
                    "items" : num_items
                }

                customer["purchases"].append(purchase)
                customer["total_spent"] += final_amount  

                multiplier = get_multiplier(customer["total_spent"])
                points_earned = (final_amount / 100) * 10 * multiplier
                customer["loyalty_points"] += points_earned  

                print(f"Points earned: {points_earned:.0f}")
                print(f"New points balance: {customer['loyalty_points']:.0f}")
                break

        if not found:
            print("Customer not found!")   

    #CHOICE 5: View top customers
    elif choice == "5":
        if len(customers) == 0:
            print("No customers yet!")
        else:
            sorted_customers = sorted(customers, key=get_total_spent, reverse=True)
            top_5 = sorted_customers[:5]
            
            print("\n=== Top 5 Customers ===")
            for rank, customer in enumerate(top_5, 1):
                tier = get_tier(customer["total_spent"])
                print(f"{rank}. {customer['name']} - R{customer['total_spent']:.2f} ({tier})")

    #CHOICE 6: Sales report
    elif choice == "6":
        print("\n---Sales Report---")

        # Initialize accumulators
        total_customers = len(customers)
        total_revenue = 0.0
        total_purchase_count = 0
        total_purchase_value = 0.0

        bronze_count = 0
        silver_count = 0
        gold_count = 0
        platinum_count = 0

        for customer in customers:
            total_revenue += customer["total_spent"]
            total_purchase_count += len(customer["purchases"])  

            # Nested loop through purchases
            for purchase in customer["purchases"]:
                total_purchase_value += purchase["amount"]

            tier = get_tier(customer["total_spent"])
            if tier == "Bronze":
                bronze_count += 1
            elif tier == "Silver":
                silver_count += 1
            elif tier == "Gold":
                gold_count += 1
            elif tier == "Platinum":
                platinum_count += 1

        # Calculate averages with division by zero protection
        if total_customers > 0:
            avg_per_customer = total_revenue / total_customers
        else:
            avg_per_customer = 0.0
                
        if total_purchase_count > 0:
            avg_purchase = total_purchase_value / total_purchase_count
        else:
            avg_purchase = 0.0   

        print(f"Total Customers: {total_customers}")
        print(f"Total Revenue: R{total_revenue:.2f}")
        print(f"Average Spend per Customer: R{avg_per_customer:.2f}")
        print(f"Total Purchases: {total_purchase_count}")
        print(f"Average Purchase Amount: R{avg_purchase:.2f}")

        print("\nCustomers by Tier:")
        print(f"  Bronze: {bronze_count}")
        print(f"  Silver: {silver_count}")
        print(f"  Gold: {gold_count}")
        print(f"  Platinum: {platinum_count}")

    #CHOICE 7: Exit
    elif choice == "7":
        print("Goodbye!")    
        break