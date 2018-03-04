def get_formated_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + middle_name +last_name
    else:
        full_name = first_name + last_name
    return full_name
stored_value = get_formated_name('muhammad ', 'anis ' )
print(stored_value)