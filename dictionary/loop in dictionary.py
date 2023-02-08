dict1 = {"name":" sneha","age":23,"course":"python"}
print(dict1)
print(type(dict1))
print(dict1.copy())
for i in dict1.keys():
    print(i)
#nested dictionary
dict2 = {
        "child1":{
            "name":"sneha",
            "age":23
        },
        "child2":{
            "course":"python",
            "address":"abc",
        },
        "child3":{
            "batch":"python",
            "phno":123344
        }
        }
print(dict2)
print(dict2["child1"]["name"])
dict2["child4"] = {"fruit1":"apple","fruit2":"orange"}
print(dict2["child4"])
print(dict2)
print(dict2["child1"].get("name"))
print(dict2.keys())
print(dict2.values())
dict2.update({"details4":{
    "fruit1":"apple",
    "fruit2":"orange"
       },
    "details5":{
        "fruit3":"grapes",
        "fruit4":"banana"
        }})
print(dict2)