print("MULTI-PLAN TELECOMMUNICATIONS COST OPTIMIZATION")

plans = [
    {
        "name": "Plan A",
        "cost": 299,
        "data": 20,
        "validity": 28,
        "extra_rate": 20
    },
    {
        "name": "Plan B",
        "cost": 399,
        "data": 30,
        "validity": 56,
        "extra_rate": 15
    },
    {
        "name": "Plan C",
        "cost": 499,
        "data": 50,
        "validity": 84,
        "extra_rate": 10
    }
]

required_data = float(input("Enter required data (GB): "))
required_validity = int(input("Enter required validity (days): "))
budget = float(input("Enter maximum budget: "))

eligible_plans = []

for plan in plans:

    if required_data > plan["data"]:
        excess_data = required_data - plan["data"]
        extra_charge = excess_data * plan["extra_rate"]
    else:
        excess_data = 0
        extra_charge = 0

    total_cost = plan["cost"] + extra_charge

    if (plan["data"] >= required_data and
            plan["validity"] >= required_validity and
            total_cost <= budget):

        eligible_plans.append(
            (plan["name"], total_cost, plan["validity"])
        )

print("\nELIGIBLE PLANS")

if eligible_plans:
    for name, cost, validity in eligible_plans:
        print(f"{name} - Total Cost: ₹{cost:.2f}, "
              f"Validity: {validity} days")

    best_plan = min(eligible_plans, key=lambda x: x[1])

    print("\nMOST ECONOMICAL PLAN")
    print("Plan:", best_plan[0])
    print("Total Cost: ₹", round(best_plan[1], 2))
    print("Validity:", best_plan[2], "days")

else:
    print("No eligible plan found within the given budget.")
