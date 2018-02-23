pet_1={'pet: ':'Dog','owner name: ':'ahsan'}
pet_2={'pet: ':'cat', 'owner name: ':'kareem'}
pet_3={'pet: ':'bird', 'owner name: ':'ali'}
pets=[pet_1, pet_2, pet_3]
for pet_list in pets:
    for k, v in pet_list.items():
     print(k + v)
    print("\n")