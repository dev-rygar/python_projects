# Practicing creation of variable and printing stuffs
lovely_loveseat_description = """Product: Lovely Loveseat.
Material: Tufted polyester blend on wood.
Dimension: 32 inches high x 40 inches wide x 30 inches deep.
Color: Red or white.

"""
lovely_loveseat_price = 254.00

stylish_settee_description = """Product: Stylish Settee.
Material: Faux leather on birch.
Dimension: 29.50 inches high x 54.75 inches wide x 28 inches deep.
Color: Black.

"""
stylish_settee_price = 180.50

luxurious_lamp_description = """Product: Luxurious Lamp.
Material: Glass and iron.
Dimension: 36 inches tall.
Color: Brown with cream shade.

"""
luxurious_lamp_price = 52

# sales tax
sales_tax = .088

# container for the sum of customers's purchase
customer_one_total = 0;
# will contain details for customer's item
customer_one_itemization = ""

customer_one_total += lovely_loveseat_price + luxurious_lamp_price

customer_one_itemization += lovely_loveseat_description + luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)

print("Customer One Total:")
print(customer_one_total)