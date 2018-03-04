magicians=['alice', 'david','carolina']
for magic in magicians:
    print(magic)
    print(magic.title())
print("\n")
magicians=['alice', 'david','carolina']
for magic in magicians:
    print(magic.title() + " was a great trick")
print("\n")
for magic in magicians:
    print(magic.title() + " was a great trick" + "\n" + "I can't wait to see your trick, " + magic.upper() + "\n")

# python avoiding these error in loop because interpretor language

print("\n")
magicians=['alice', 'david','carolina']
for magic in magicians:
    print(magic)
print("python read " + magic + " because value store in last.")