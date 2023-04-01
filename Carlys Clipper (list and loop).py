# Part of python - data analyst project
# Putting Loop, list, list comprehension into practice
# Provided list and variables
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# My code starts from here
# 1. will loop through list prices and will sum it up and save it to total_price variable
total_price = 0
for price in prices:
  total_price += price

# 2. Getting the average price of total_price, by using len.
average_price = total_price / len(prices)
# 3. Printing average price
print("Average Haircut Price:", average_price)
# 4. The average price is more expensive that Carly thought, so he asked me to cut all the price by 5 using list comprehension.
new_prices = [price - 5 for price in prices]
# Printing the new price 
print(new_prices)

# 5. Carly wants to make sure that Carly's Clippers is profitable endeavor, so I'll have to create a new variable and do for loop to get the total revenue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue:", total_revenue)
# 6. Finding the average revenuw
average_daily_revenue = total_revenue / 7

# 7. Carly thinks that she can bring more customer by advertising haircuts that is under 30 dollars; using list comprehesion I will generate every hairstyle that is under 30 dollars.
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices) - 1) if new_prices[i] < 30]

print(cuts_under_30)