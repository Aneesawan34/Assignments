available_toppiings=['mushrooms','olives', 'green peppers', 'pepperoni',' pineapple', 'extra cheese']
requested_toppings=['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppiings:
        print("adding " + requested_topping + ".")
    else:
        print("sorry, we have not " + requested_topping + ".")