polls = True
list = []
while polls:
    visit = input("if you could visit one place in the world:(yes/no)\t")
    if visit == 'yes':
        which_city = input("where would you go:\t")
        list.append(which_city)

    if visit == 'no':
        print("\nyou did not select yes")
        polls = False
print("--- result---")
for city_list in list:
    print(city_list)