# In this script, you should pay differently by their sales. 
# If the saleman's sales were over the quota than give him different commission based on his performance ratio
# base quota is 5000
# price os 1 unit of sales 500
# regular commision rate is 0.2
# promotion commision rate is 0.5
# Get input from salesman about this month's sales.
# Calculate sale person's total commision payment.


base_quota = 5000
sales = int(input("Please enter your sales: "))

if sales > base_quota:
    total_commision_payment = 1000 + (sales - base_quota) * 0.5
elif sales == base_quota:
    total_commision_payment = 1000
else:
    total_commision_payment = sales * 0.2
