#lovely loveseat
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

lovely_loveseat_price = 254.00

#stylish settee
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

stylish_settee_price = 180.50

#luxurious lamp
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_price = 52.15

#taxes
sales_tax = 0.088

#customer 1
customer_one_total = 0
customer_one_itemization = ""

#customer 1 purchase loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

print(customer_one_total)
print(customer_one_itemization)


#customer 1 purchase lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += '\n' + luxurious_lamp_description

print(customer_one_total)
print(customer_one_itemization)

#customer one tax

customer_one_tax = customer_one_total * sales_tax
print('Tax:', customer_one_tax)

#customer one total
customer_one_total += customer_one_tax
print("After tax:", customer_one_total)

#receipt
print('Customer One Items:')
print(customer_one_itemization)

print('Customer One Total:')
print(customer_one_total)