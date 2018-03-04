favourite_language={'jen':'python', 'sarah':'c', 'edward':'ruby', 'phil':'python'}
print("The following values has been mentioned:\n")
for value in favourite_language.values():
    print(value)

print("\n\n")
for name2 in set(favourite_language.values()): #set is for stop repitition
    print(name2)