favourite_language={'jen':'python','sarah':'c','edward':'ruby'}
freinds=['phils', 'sarah']
for name in favourite_language.keys():
    print(name)
    if name in freinds:
        print("Hi " + name + "i see your Favourite Book is " + favourite_language[name])