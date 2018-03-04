def name(first_name, last_name):
    full_name = first_name + last_name
    return full_name
while True:
    print("enter your name:")
    f_name = input("First name:\t")
    if f_name == 'q':
        break
    l_name = input("Last name:\t")
    if l_name == 'q':
        break
    print("hello "+ name())
