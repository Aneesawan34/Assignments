# using active variable

promt_topping_pizza ="Enter a topping for your pizza:\t"

active=True
while active:
    message=input(promt_topping_pizza)
    if message =="quit":
        active = False
    else:
        print(message)


# using break


#
# promt_topping_pizza ="Enter a topping for your pizza:\t"
# while True:
#     message = input(promt_topping_pizza)
#     if message == "quit":
#         break
#     else:
#         print(message)