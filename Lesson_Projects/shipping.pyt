# Learning Project Four: Sal's Shipping
# Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.
# In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

#Item variables

weight = 1.5

#Shipping conditionals

cost = 0
flat_rate = 0
using_premium = True
using_ground = False

#determine if using premium
if using_premium == True:
  flat_rate += 125
else:
  flat_rate += 20

#determine if using drone or ground

if using_ground == True:
  if weight <= 2:
    cost = weight * 1.50 + flat_rate
  elif weight > 2 and weight <= 6:
    cost = weight * 3 + flat_rate
  elif weight > 6 and weight <= 10:
    cost = weight * 4 + flat_rate
  else:
    cost = weight * 4.75 + flat_rate
else:
  if weight <= 2:
    cost = weight * 4.50
  elif weight > 2 and weight <= 6:
    cost = weight * 9
  elif weight > 6 and weight <= 10:
    cost = weight * 12
  else:
    cost = weight * 14.25

print(cost)