users = {'aeinstein':{'first':'albert','last':'einstein','location':'princeton'},
         'mcurie':{'first':'ABC','last':'CDE','location':'PTa Nai'}
         }
for name, details in users.items():
    print(name)
    for inner_name, inner_detail in details.items():
        print(inner_name + ":" + inner_detail)
    print("\n")
