number_list=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
for number_th in number_list:
    if number_th == '1':
        print(number_th + "st")
    elif number_th == '2':
        print(number_th + "nd")
    elif number_th == '3':
        print(number_th + "rd")
    else:
        print(number_th + "th")