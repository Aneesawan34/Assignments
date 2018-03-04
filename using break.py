promt = "Please enter a name of city you have visited: \t"
# active = True
# while active:
while True:
    city = input(promt)
    if city == "quit":
        # active = False
        break
    else:
        print("I would love to go to " + city + "\n")