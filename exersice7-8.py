sandwich_order = ['chicken', 'club', 'egg']
print("list of sandwich:\t" + str(sandwich_order) + "\n")
finished_sandwich = []
while sandwich_order:
    pick_sandwich = sandwich_order.pop()
    print("I made to you "+ pick_sandwich.upper() + " sandwich.")
    finished_sandwich.append(pick_sandwich)
print("\n")
for made_sandwich in finished_sandwich:
    print(made_sandwich.upper() + " sandwich was made.")
