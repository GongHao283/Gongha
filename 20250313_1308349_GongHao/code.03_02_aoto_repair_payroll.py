# This script will calculate payroll in different situation
# Set base hour
base_hour = 40
# Overtime multiplier
ot_multiplier = 1.5
# Money per hour
payrate_per_hour = 1000
# Get work hour for this week
hour = int(input(" Please enter the work hour that you worked this week:"))
# Calculate the payroll if worker work more than base hour multiply hourly payrate
if hour > base_hour:
    overtime_hour = hour - base_hour
    overtime_pay = overtime_hour * ot_multiplier * payrate_per_hour
    total_payment = base_hour * payrate_per_hour + overtime_pay
    print(f"Your work {overtime_hour} than {base_hour}, so you got {ot_multiplier:0%} rate for your extra overload. Payment for the overtime was {overtime_pay:,.2f} yuan, your total payment is {total_payment:,.2f} yuan")
else:
    total_payment = (hour * payrate_per_hour)
print(f"Your total payment is {total_payment}")
# payment = hour * payrate_per_hour
# ot_payment = (hour - base_hour) * ot_multiplier * payrate_per_hour
# total_payment = payment + ot_payment