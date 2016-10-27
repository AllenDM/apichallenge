#   CODE 2040 API Challenge
#   
#   Author: AllenDM Allen Moody
import ast
import requests

token = input("Enter API Token: ")

# Step 1
register = {'token' : token, 'github': 'https://github.com/AllenDM/apichallenge'}
requests.post("http://challenge.code2040.org/api/register", data = register)

# Step 2
plainToken = {'token': token}
r = requests.post("http://challenge.code2040.org/api/reverse", data = plainToken)
reversedString = r.text[::-1]
reverseSolution = {'token': token, 'string': reversedString}
requests.post("http://challenge.code2040.org/api/reverse/validate", data = reverseSolution)

# Step 3
d = requests.post("http://challenge.code2040.org/api/haystack", data = plainToken)
needleMap = ast.literal_eval(d.text)
needleIndex = (needleMap['haystack'].index(needleMap['needle']))
needleSolution = {'token': token, 'needle': needleIndex}
requests.post("http://challenge.code2040.org/api/haystack/validate", data = needleSolution)