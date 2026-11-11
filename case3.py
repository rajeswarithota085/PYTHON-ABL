print("HOSPITAL BILLING AND PATIENT CLASSIFICATION")

patient_name = input("Enter patient name: ")

consultation = float(
    input("Enter consultation charge: ₹")
)

diagnostic = float(
    input("Enter diagnostic charge: ₹")
)

treatment = float(
    input("Enter treatment charge: ₹")
)

# Calculate total bill
total_bill = consultation + diagnostic + treatment

# Calculate concession
if total_bill > 10000:
    concession = total_bill * 0.10
else:
    concession = total_bill * 0.05

# Calculate final bill
final_bill = total_bill - concession

print("\n========== BILL DETAILS ==========")
print("Patient Name:", patient_name)
print("Total Bill: ₹", round(total_bill, 2))
print("Concession: ₹", round(concession, 2))
print("Final Bill: ₹", round(final_bill, 2))

# Payment
paid = float(input("Enter amount paid: ₹"))

# Payment validation and classification
if paid < 0 or paid > final_bill:
    print("Payment Status: Invalid Amount")
elif paid == final_bill:
    print("Payment Status: PAID")
elif paid > 0:
    print("Payment Status: PARTIALLY PAID")
else:
    print("Payment Status: PENDING")

print("==================================")
