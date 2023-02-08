my_dictionary = {
    "name":"sneha",
    "age":23,
    "address":"abcde"
}
print(my_dictionary)
print(my_dictionary["name"])
# #or
x = my_dictionary.get("age")
print(x)
#to get keys
x = my_dictionary.keys()
print(x)
#to get values
x = my_dictionary.values()
print(x)
# #to get iems as a tuple
x = my_dictionary.items()
print(x)
# #to change the values
my_dictionary["age"] = 22
print(my_dictionary)
# #update
my_dictionary.update({"address":"parambil","course":"python","batch":"2022"})
print(my_dictionary)
# #add
my_dictionary["phoneno"] = 123456799
print(my_dictionary)
#to remove specified key
my_dictionary.pop("batch")
print(my_dictionary)
# or
del my_dictionary["age"]
print(my_dictionary)
#to remove last value
my_dictionary.popitem()
print(my_dictionary)
# #to remove all the items we can use 'del my_keyword' or clear()
my_dictionary.clear()
print(my_dictionary)