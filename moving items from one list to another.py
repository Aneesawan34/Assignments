unconfirmed_user=['ali', 'asghar', 'ahmed', 'hassan']
confirmed_user=[]
while unconfirmed_user:
    currrent_user = unconfirmed_user.pop()
    print("Confirmed user are: " + currrent_user)
    confirmed_user.append(currrent_user)
for list in confirmed_user:
    print(list)




# first_list = ['ali', 'asghar', 'ahmed', 'qaseer']
# second_list = ['qaheem', 'ali', 'hassan', 'ahmed']
# for compare in first_list:
#     for list in second_list:
#         if list==compare:
#             print(list)
    # or we can do with
    # if compare in second_list:
    #     print(compare)