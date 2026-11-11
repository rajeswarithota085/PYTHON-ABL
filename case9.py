print("MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")

budget = float(input("Enter travel budget in INR: ₹"))

conversion_fee_percentage = float(
    input("Enter conversion fee percentage: ")
)

n = int(input("Enter number of expenses: "))

expenses = []

for i in range(n):
    print(f"\nExpense {i + 1}")

    category = input("Enter expense category: ")
    currency = input("Enter currency: ")
    amount = float(input("Enter amount: "))
    exchange_rate = float(
        input(f"Enter exchange rate of 1 {currency} in INR: ")
    )

    # Currency conversion
    converted_amount = amount * exchange_rate

    # Conversion fee
    conversion_fee = (
        converted_amount * conversion_fee_percentage / 100
    )

    final_amount = converted_amount + conversion_fee

    expenses.append({
        "category": category,
        "currency": currency,
        "original": amount,
        "converted": converted_amount,
        "fee": conversion_fee,
        "final": final_amount
    })

total_expense = sum(
    expense["final"] for expense in expenses
)

# Find largest expense category
largest_expense = max(
    expenses,
    key=lambda x: x["final"]
)

print("\n========== TRAVEL EXPENSE REPORT ==========")

for expense in expenses:
    print(
        f"{expense['category']} | "
        f"{expense['original']:.2f} {expense['currency']} | "
        f"Converted: ₹{expense['converted']:.2f} | "
        f"Fee: ₹{expense['fee']:.2f} | "
        f"Final: ₹{expense['final']:.2f}"
    )

print("-------------------------------------------")
print(f"Total Travel Expense: ₹{total_expense:.2f}")
print(f"Travel Budget: ₹{budget:.2f}")

if total_expense <= budget:
    print("Status: WITHIN BUDGET")
else:
    print("Status: BUDGET EXCEEDED")

print(
    "Largest Expense Category:",
    largest_expense["category"]
)

print(
    f"Largest Expense: ₹{largest_expense['final']:.2f}"
)

print("===========================================")
