# This program calculates sales commissions

# Create a variable to control the loop
keep_going = 'y'
# Calculate a series of commissions
while keep_going == 'y':

# Get a salesperson's sales and commission rate
    # Calculate the commission
    # Display the commission
    # See if the user wants to calculate another one

    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))
    commission = sales * comm_rate
    print('The commission is $', format(commission, ',.2f'), sep='')
    keep_going = input('Do you want to calculate another ' + 'commission (Enter y for yes): ')