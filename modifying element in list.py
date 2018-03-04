#changing element

motercycle=['honda', 'suzuki', 'yamaya']
print(motercycle[0])
motercycle[0]='ducati'
print(motercycle[0])

#Adding element by append1

print("\n")
motercycle=['honda', 'suzuki', 'yamaya']
print(motercycle) #3 element of list cant read now(you cant jump to 3 element)
motercycle.append('ducati')
print(motercycle)
print(motercycle[3]) #now you can jump or reach to 3 element

#adding element by insert2

print("\n")
print(motercycle)
motercycle.append('Honda')
print(motercycle)
motercycle.append('Suzuki')
print(motercycle)
motercycle.append('yamaha')
print(motercycle)

#adding and removing by pop element3

print("\n")
game=['mario 1', 'mario 2', 'mario 3']
print(game)
game.insert(1,'mario 1.5 new version and mario 2 will be gone soon')
print(game)
game.pop(2)
game[1]='mario 1.5 new version updated'
print(game)

#removing element by remove4

print("\n")
print("List of motercycles given below:")
motercycle=['Honda', 'suzuki', 'yamaha']
print(motercycle)
too_expensive='yamaha'
motercycle.remove(too_expensive)
print(motercycle)
print("\nThe " + too_expensive + " is too expensive for me")
print(motercycle)
budget='Honda'
motercycle.remove(budget)
print("\nThe " + budget + " is for my budget")
