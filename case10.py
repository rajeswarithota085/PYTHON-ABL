venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificates = float(input("Enter certificate cost: "))

participants = int(input("Enter number of participants: "))
fee = float(input("Enter registration fee per participant: "))
sponsorship = float(input("Enter sponsorship amount: "))

# Calculate total cost
total_cost = venue + equipment + catering + transport + certificates

# Calculate participant contribution
contribution = participants * fee

# Calculate shortfall
shortfall = total_cost - contribution - sponsorship

if shortfall < 0:
    shortfall = 0

# Calculate minimum registrations
remaining_cost = total_cost - sponsorship

if remaining_cost <= 0:
    break_even = 0
elif fee <= 0:
    break_even = -1
else:
    break_even = int(remaining_cost / fee)

    if break_even * fee < remaining_cost:
        break_even = break_even + 1

# Display results
print("\n--- Campus Event Financial Report ---")
print("Total Event Cost:", total_cost)
print("Participant Contribution:", contribution)
print("Sponsorship:", sponsorship)
print("Sponsorship Shortfall:", shortfall)

if break_even == -1:
    print("Break-even registrations: Not possible")
else:
    print("Minimum Registrations:", break_even)

if contribution + sponsorship >= total_cost:
    print("Status: Financially Feasible")
else:
    print("Status: Additional Funds Required")
