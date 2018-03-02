movie_ticket =int(input("Enter age:\t"))

if movie_ticket < 3:
    print(" your ticket is free")
elif movie_ticket >= 3 and movie_ticket <= 12:
    print(" your ticket price  is $10")
else:
    print(" your ticket price is $15")