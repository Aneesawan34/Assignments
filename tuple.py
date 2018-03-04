dimensions=(200, 50)
print(dimensions)
print(dimensions[0])
print(dimensions[1])
# dimensions[1]=100
# print(dimensions[1])

#Looping through all Values in a tuple

print("\n")
dimensions=(200, 50)
for list_tuple in dimensions:
    print(list_tuple)

#Writing over a tuple
dimensions=(200, 50)
print("\n"+"Original Dimension:")
for dimension in dimensions:
    print(dimension)
 #modified
dimensions=(100, 400)
print("\n"+ "Modified Dimension:")
for dimension in dimensions:
    print(dimension)