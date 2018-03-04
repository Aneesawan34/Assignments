favourite_language={'jen':['python', 'ruby'], 'sarah':['c', 'Go'], 'edward':['c++', 'C sharp']}
for name, languages in favourite_language.items():
   print(name + "'s favouritr languages are:")
   for language in languages:
       print("\t" + language)