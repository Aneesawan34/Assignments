dictionary = {}
action_list = True
while action_list:
    name = input("Please tell me your name:\t")
    mountain_name = input("please tell me where would you like to travel:\t")
    dictionary[name]=mountain_name
    repeat = input("would you add name more ? (yes/no):\t")
    if repeat == 'no':
        action_list = False
        print("---Result---")
        print("\n")
for person, city in dictionary.items():
    print(person + " would like to travel " + city)