flag = True
while flag:
    message = input("I will back to you until you write quit: \t")
    if message == "quit":
        flag = False
    else:
        print(message)