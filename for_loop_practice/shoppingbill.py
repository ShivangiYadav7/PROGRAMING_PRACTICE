#Shopping Bill Generator⭐⭐


print("\n==== SHOPPING BILL GENERATOR ====")

# User se puchte hain kitne items hain
total_items = int(input("How many items do you want to buy? "))

total_bill = 0

# Loop items ke quantity par chalega
for i in range(1, total_items + 1):
    print(f"\n--- Item {i} ---")
    item_name = input("Enter item name: ")
    price = float(input(f"Enter price for {item_name}: ₹"))
    
    total_bill += price  # Total me price add kar rahe hain

print("\n" + "=" * 30)
print(f"TOTAL BILL AMOUNT = ₹{total_bill}")
print("===============================")
