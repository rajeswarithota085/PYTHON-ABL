# Case 10: Campus Event Financial Planning

## Introduction

The Campus Event Financial Planning program calculates the total cost of
organizing a campus event and checks whether participant registration
fees and sponsorship can cover the expenses.

## Features

-   Accepts venue, equipment, catering, transport, and certificate
    costs.
-   Calculates total event cost.
-   Calculates participant contribution from the number of participants
    and registration fee.
-   Calculates any additional funds required after sponsorship and
    participant contributions.
-   Calculates the minimum number of registrations needed to cover the
    cost after sponsorship.
-   Displays whether the event is financially feasible.

## Requirements

-   Python 3
-   No external libraries are required.

## How to Run

1.  Save the program as `case10.py`.

2.  Open a terminal in the folder containing the file.

3.  Run:

    ``` bash
    python case10.py
    ```

4.  Enter the requested costs, participant count, registration fee, and
    sponsorship amount.

## Input Details

-   Venue cost
-   Equipment cost
-   Catering cost
-   Transport cost
-   Certificate cost
-   Number of participants
-   Registration fee per participant
-   Sponsorship amount

## Calculations

-   **Total Event Cost** = Venue + Equipment + Catering + Transport +
    Certificates
-   **Participant Contribution** = Number of Participants × Registration
    Fee
-   **Sponsorship Shortfall** = Total Event Cost − Participant
    Contribution − Sponsorship\
    If the result is negative, the shortfall is displayed as zero.
-   **Minimum Registrations** = The smallest number of registrations
    required to cover the remaining cost after sponsorship.

## Output

The program displays the total event cost, participant contribution,
sponsorship amount, sponsorship shortfall, minimum registrations, and
financial status.

## Conclusion

This program helps event organizers estimate expenses, understand
funding needs, and plan the number of registrations required to make a
campus event financially feasible.
