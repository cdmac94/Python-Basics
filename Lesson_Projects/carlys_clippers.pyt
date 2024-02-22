# Learning Project Seven: Carly's Clippers
# You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. Your job is to go through the lists of data that have been collected in the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.

# Hairstyle variables and sales numbers

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Finding average hairstyle price

total_price = 0
for price in prices:
  total_price = total_price + price

#print(total_price)

average_price = total_price / len(prices)
print("Average Haircut Price: ", average_price)

# Reduce prices for sale

new_prices = []

for price in prices:
  new_prices.append(price - 5)
print(new_prices)

# Calculate last weeks sales and daily average

total_revenue = 0

for i in range (0, len(hairstyles)):
  total_revenue += (prices[i] * last_week[i])
print("Total Revenue: ", total_revenue)

average_daily_revenue = total_revenue / 7

print("Average daily revenue: ", average_daily_revenue)

# Determine which haircuts should be advertised

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices) - 1) if new_prices[i] < 30]

print(cuts_under_30)
