sandwich_order = ['chicken', 'club', 'egg', 'pastrami']
finished_sandwich = []

print("list of sandwich:\t" + str(sandwich_order) + "\n")
print("pastrami is remove from list")
sandwich_order.remove('pastrami')
while sandwich_order:
    pick_sandwich = sandwich_order.pop()
    print("I made to you "+ pick_sandwich.upper() + " sandwich.")
    finished_sandwich.append(pick_sandwich)
print("\n")
for made_sandwich in finished_sandwich:
    print(made_sandwich.upper() + " sandwich was made.")
