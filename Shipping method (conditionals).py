# Another conditional statement challenge/project
# In this project, you’ll build a program that will take the weight 
# of a package and determine the cheapest way to ship that package using Sal’s Shippers
weight = 41.5

ground_shipping = 0

# ground shipping premium doesn't charge per weight but has higher flat rate, which is $125
ground_shipping_premium = 125

# drone shipping has no flat charge but the rate per weight is triple
drone_shipping = 0

# Default value is equal to ground shipping flat charge.
flat_charge = 20

# Price per pound will be updated base on the weight of package.
price_per_pound = 0

# Ground shipping
if weight <= 2:
  price_per_pound = 1.50
elif weight > 2 and weight <= 6:
  price_per_pound = 3.00
elif weight > 6 and weight <= 10:
  price_per_pound = 4.00
elif weight > 10:
  price_per_pound = 4.75
else:
  print('error in ground shipping')

# total cost of ground shipping
ground_shipping = weight * price_per_pound + flat_charge

# Drone Shipping
if weight <= 2:
  price_per_pound = 4.50
elif weight > 2 and weight <= 6:
  price_per_pound = 9.00
elif weight > 6 and weight <= 10:
  price_per_pound = 12.00
elif weight > 10:
  price_per_pound = 14.25
else:
  print('Error in drone shipping')

# total of drone shipping
drone_shipping = weight * price_per_pound

# Will printout now the total cost of shipping per shipping method.
print('Total cost of Ground Shipping:', ground_shipping)
print('Total cost of Ground Shipping Premium:', ground_shipping_premium)
print('Total cost of Drone Shipping:', drone_shipping)

if ground_shipping < ground_shipping_premium and ground_shipping < drone_shipping:
  print("The cheapest shipping method is: Ground Shipping!")
elif ground_shipping_premium < ground_shipping and ground_shipping_premium < drone_shipping:
  print("The cheapest shipping method is: Ground Shipping Premium!")
elif drone_shipping < ground_shipping and drone_shipping < ground_shipping_premium:
  print("The cheapest shipping method is: Drone Shipping!")
else:
  print('Error in: conditional statement that checks that cheapest method!')