def build_person(first_name, last_name):
    person = {'first':first_name, 'last':last_name}
    return person
stored_value = build_person('muhammad anis ', 'ur rehman')
for name, value in stored_value.items():
    print(name + "\t" + value)