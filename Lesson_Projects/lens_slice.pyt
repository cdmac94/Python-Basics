# Learning Project Six: Len's Slice
#You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.


# Basic pizza variables
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)

# Pizza menu with prices
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]


# Arrange pizza by price to find cheapest and priciest slice
pizza_and_prices.sort()

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

# Sell priciest slice

pizza_and_prices.pop()

# Replace sold slice with new peppers slice

pizza_and_prices.insert(4, [2.5, "peppers"])

# Three poor mice want the cheapest three slices

three_cheapest = pizza_and_prices[0:3]



print(three_cheapest)

