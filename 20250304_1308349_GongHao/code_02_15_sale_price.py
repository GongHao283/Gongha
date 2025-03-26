# This program gets an item's original price and calculates its sale price, with a 20% discount.
# Display amount of cut(discount), discounted price.
# Set discount
discount = 0.2
# Get a original price of a product
price_ori = int(input("Please enter original price of the product you choice:"))
# Calculate the amount of discount
amount_discount = price_ori * discount
# Calculate the discounted price
price_disc = price_ori - amount_discount
# Display amount of discount and discounted price with message. Number should, after 3 digits, and show 2 digits after decimal point
print(f"What you selected is {price_ori:,.2f} Yuan, this time you do {discount:.0%} discount, it means you can save {amount_discount:,.2f} Yuan, and you only need to pay {price_disc:,.2f} Yuan.")