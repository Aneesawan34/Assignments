dictionary_1= {"name1":'ali', 'class':'4th'}
dictionary_2={'name2':'akhber', 'class':'5th'}
dictionary_3={'name':'akhter',  'class':'6th'}
list_of_people=[dictionary_1, dictionary_2, dictionary_3]
for list in list_of_people:
    for key, value in list.items():
        print("key:" + key)
        print("value:" + value)