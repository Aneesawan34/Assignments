favourite_language={'jen':'python','sarah':'c','edward':'ruby', 'phill':'python'}
list_of_people=['sarah', 'admird', 'phill']
for people in favourite_language:
    if people in list_of_people:
        print("Thank you " + people + " for responding " + favourite_language[people])
    else:
        print(people.title() + " you are Inviting " + "for " + favourite_language[people])