#copy slice a list
my_foods=['pizza', 'falafel', 'carrot cat',]
my_favorite_food=my_foods[:]
print(my_foods)
print(my_favorite_food)

#copying slice a list and append

print("\n")
my_foods.append('icecreem')
print(my_foods)
my_favorite_food.append('cannoli')
print(my_favorite_food)

#just copy list

print("\n")
my_foods=['pizza', 'falafel', 'carrot cat',]
my_favorite_food=my_foods
my_foods.append('icecreem')
print(my_foods)
print(my_favorite_food)