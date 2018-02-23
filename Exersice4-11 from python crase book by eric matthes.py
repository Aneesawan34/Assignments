pizzas=['chicken tikka', 'fajita', 'arabian', 'creamy']
favarite_pizzas=pizzas[:]
pizzas.append('vagitable')
favarite_pizzas.append('pepperoni')
print(pizzas)
print(favarite_pizzas)
print("\n")
print("My pizzaa are:")
for list_pizza in pizzas:
    print(list_pizza)
print("\n")
print("My favorite pizzas are:")
for favarite_pizzas_list in favarite_pizzas:
    print(favarite_pizzas_list)