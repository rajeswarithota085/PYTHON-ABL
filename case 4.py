print("EMPLOYEE PAYROLL SYSTEM")

name = input("Enter employee name: ")
basic = float(input("Enter basic pay: "))
overtime_hours = float(input("Enter overtime hours: "))
incentive = float(input("Enter incentive amount: "))

# Calculate allowances
hra = basic * 0.20
da = basic * 0.10

# Calculate overtime pay
overtime_pay = overtime_hours * 200

# Calculate gross salary
gross_salary = basic + hra + da + overtime_pay + incentive

# Calculate progressive deduction
if gross_salary <= 20000:
    deduction_rate = 0.05
elif gross_salary <= 40000:
    deduction_rate = 0.10
else:
    deduction_rate = 0.15

deduction = gross_salary * deduction_rate

# Calculate net salary
net_salary = gross_salary - deduction

# Salary statement
print("\n========== SALARY STATEMENT ==========")
print("Employee Name :", name)
print("Basic Pay     : Rs.", round(basic, 2))
print("HRA           : Rs.", round(hra, 2))
print("DA            : Rs.", round(da, 2))
print("Overtime Pay  : Rs.", round(overtime_pay, 2))
print("Incentive     : Rs.", round(incentive, 2))
print("--------------------------------------")
print("Gross Salary  : Rs.", round(gross_salary, 2))
print("Deduction     : Rs.", round(deduction, 2))
print("Net Salary    : Rs.", round(net_salary, 2))
print("======================================")
