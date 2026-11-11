bills = []

n = int(input("Enter number of months: "))

for i in range(n):
    print("\nMonth", i + 1)

    units = float(input("Enter electricity consumption (units): "))

    # Calculate slab-wise charge
    if units <= 100:
        charge = units * 2

    elif units <= 200:
        charge = (100 * 2) + ((units - 100) * 3)

    else:
        charge = (100 * 2) + (100 * 3) + ((units - 200) * 5)

    # Add fixed charge
    bill = charge + 50

    # Apply surcharge or rebate
    if units > 300:
        bill = bill + (bill * 0.10)
    elif units < 100:
        bill = bill - (bill * 0.05)

    bills.append(bill)

    print("Final Bill: Rs.", round(bill, 2))

print("\n--- MONTHLY BILL ANALYSIS ---")

for i in range(n):
    print("Month", i + 1, ": Rs.", round(bills[i], 2))

    if i > 0:
        increase = ((bills[i] - bills[i - 1]) / bills[i - 1]) * 100

        if increase > 20:
            print("Status: Unusual increase")
        else:
            print("Status: Normal")
