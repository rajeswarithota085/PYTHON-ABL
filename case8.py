print("MANUFACTURING COST AND PROFITABILITY ANALYSIS")

quantity = int(input("Enter quantity produced: "))

material_per_unit = float(
    input("Enter material cost per unit: ₹")
)

labour_per_unit = float(
    input("Enter labour cost per unit: ₹")
)

machine_per_unit = float(
    input("Enter machine cost per unit: ₹")
)

wastage_percentage = float(
    input("Enter wastage percentage: ")
)

selling_price_per_unit = float(
    input("Enter selling price per unit: ₹")
)

target_profit_percentage = float(
    input("Enter target profit percentage: ")
)

# Cost calculations
material_cost = quantity * material_per_unit

wastage_cost = material_cost * wastage_percentage / 100

labour_cost = quantity * labour_per_unit

machine_cost = quantity * machine_per_unit

total_cost = (
    material_cost
    + wastage_cost
    + labour_cost
    + machine_cost
)

# Sales and profit
sales_value = quantity * selling_price_per_unit

profit = sales_value - total_cost

if total_cost > 0:
    profit_percentage = (profit / total_cost) * 100
else:
    profit_percentage = 0

print("\n========== PRODUCTION REPORT ==========")
print(f"Quantity Produced: {quantity}")
print(f"Material Cost: ₹{material_cost:.2f}")
print(f"Wastage Cost: ₹{wastage_cost:.2f}")
print(f"Labour Cost: ₹{labour_cost:.2f}")
print(f"Machine Cost: ₹{machine_cost:.2f}")
print(f"Total Production Cost: ₹{total_cost:.2f}")
print(f"Total Sales Value: ₹{sales_value:.2f}")
print(f"Profit: ₹{profit:.2f}")
print(f"Profit Percentage: {profit_percentage:.2f}%")

if profit_percentage >= target_profit_percentage:
    print("Status: PROFIT TARGET ACHIEVED")
else:
    print("Status: PROFIT TARGET NOT ACHIEVED")

print("=======================================")
