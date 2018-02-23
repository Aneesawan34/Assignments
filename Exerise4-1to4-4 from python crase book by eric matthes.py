# Exersice#4-4

for value in range(1,20+1):
    print(value)
    # Exersice#4-5

print("\n")
list=[]
for value in range(1,20+1):
    # print(value)
    list.append(value)
print(list)
print("\n")
for loop_list in list:
    print(loop_list)
print("\n")
print(len(list))
print(min(list))
print(max(list))
print(sum(list))

# Exersice#4-6

print("\n")
for odd_number in range(1,20+1,2):
    print(odd_number)

# Exersice#4-7
list_of_threes=[]
print("\n")
for multiple_of_threes in range(3,30+1,3):
    # print(multiple_of_threes)
    list_of_threes.append(multiple_of_threes)
print(list_of_threes)
print("Total multiples are " + str(len(list_of_threes)))
print("small value is " + str(min(list_of_threes)))
print("last value is " + str(max(list_of_threes)))


# # Exersice#4-2one million
# print("\n")
# for one_million in range(1,1000000):
#     print(one_million)