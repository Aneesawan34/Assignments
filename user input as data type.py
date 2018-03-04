your_name ="what is your name: "
your_age="What is your age: "
name = input(your_name)
if name == "anees":
    age = int(input(your_age))
    if age <= 18:
        print(name + "you cannot inter in a part bacause your age is greather than " + str(age))
    elif age> 18 and age <= 25:
        print(name + " you can enter in a park bacause your age is " + str(age))
    elif age > 25 and age < 30:
        print(name + " you can not allow because your age is greather then " + str(age) + " and less than 30")
    else:
        print(name + " your age is over, that is " + str(age) + " so you not allowed sorry!")
else:
    print("please registered yourself")