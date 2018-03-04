user={'username':'ali1234','first_name':'ali','last_name':'ahmed'}
for key, value in user.items():
    print("\nkey: " +key)
    print("value: " + value)


###########
print("\n\n")

favourite_language={'jen':'python','sarah':'c','edward':'ruby'}
for name, language in favourite_language.items():
    print(name + "'s favourite book is " + language)

print("\n\n")

favourite_language={'jen':'python','sarah':'c','edward':'ruby'}
for name in favourite_language.keys():
    print(name)