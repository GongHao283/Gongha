# Get the desired future value
future_value = float(input("Enter the amount of money you want to make: "))
# Get the annual future rate
rate = float(input("Enter the annual interest rate: "))
# Get the number of years that the money will appreciate
years = int(input("Enter the number of years the money will grow: "))
# Calculate the amount needed to deposit
presnet_value = future_value / (1.0 + rate)**years
# Display the amount needed to deposit
print(f"If you want to make {future_value:,.2f} Yuan in {years} years, with annual interest rate as {rate:,.2f}, you need to deposit today {presnet_value:,.2f} Yuan now.")