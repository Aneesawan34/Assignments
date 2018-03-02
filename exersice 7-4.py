message=""
promt_topping_pizza ="Enter a topping for your pizza:\t"
while message !="quit":
    message = input(promt_topping_pizza)
    if message == "quit":
        print("you are quit")
    else:
        print("You would add " + message + " to your pizza.")