print("RAILWAY FARE AND RESERVATION CALCULATOR")

n = int(input("Enter number of passengers: "))

total_revenue = 0

for i in range(n):
    print(f"\nPassenger {i + 1}")

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter travel distance (km): "))

    travel_class = input(
        "Enter class (Sleeper/AC3/AC2): "
    ).lower()

    cancelled = input(
        "Is the ticket cancelled? (yes/no): "
    ).lower()

    # Distance-based fare
    if distance <= 100:
        rate = 1.50
    elif distance <= 300:
        rate = 1.25
    else:
        rate = 1.00

    fare = distance * rate

    # Class multiplier
    if travel_class == "sleeper":
        multiplier = 1.0
    elif travel_class == "ac3":
        multiplier = 1.5
    elif travel_class == "ac2":
        multiplier = 2.0
    else:
        print("Invalid class.")
        continue

    fare = fare * multiplier

    # Age concession
    if age < 5:
        fare = 0
    elif age <= 12:
        fare = fare * 0.50
    elif age >= 60:
        fare = fare * 0.60

    # Reservation charge
    reservation_charge = 50
    fare_before_cancellation = fare + reservation_charge

    # Cancellation penalty
    if cancelled == "yes":
        penalty = fare_before_cancellation * 0.20
        final_amount = fare_before_cancellation - penalty
    else:
        penalty = 0
        final_amount = fare_before_cancellation

    total_revenue += final_amount

    print("\n--- FARE DETAILS ---")
    print("Passenger Name:", name)
    print("Age:", age)
    print("Distance:", distance, "km")
    print("Class:", travel_class)
    print("Base Fare: ₹", round(fare, 2))
    print("Reservation Charge: ₹", reservation_charge)
    print("Cancellation Penalty: ₹", round(penalty, 2))
    print("Final Fare: ₹", round(final_amount, 2))

print("\nTotal Amount: ₹", round(total_revenue, 2))
