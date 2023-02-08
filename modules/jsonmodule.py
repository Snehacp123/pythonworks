# import json
# # import os
# # import  random
# print(dir(json))
import json
x = '{"name":"sneha","age":22,"course":"python"}'
print(type(x))
#parsing json to python
y = json.loads(x)
print(y)
print(type(y))
x = {"name":"sneha","age":22,"course":"python"}
print(type(x))
#parsing python to json
y = json.dumps(x)
print(y)
print(type(y))
