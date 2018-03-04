current_user=['Ali', 'asghar', 'Ahmed', 'sheikh']
new_user=['asghar', 'zahid', 'hassan', 'nadir']

for compare_user in current_user:
    if compare_user in new_user:
        print("This user is available")
    else:
        print("you need to add new user")