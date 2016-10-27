#   CODE 2040 API Challenge 
#   Author: AllenDM Allen Moody
import ast
import requests

# Step 1
token = input("Enter API Token: ")
requests.post("http://challenge.code2040.org/api/register", data = {'token' : token, 'github': 'https://github.com/AllenDM/apichallenge'})

# Step 2
plainToken = {'token': token}
reverseData = requests.post("http://challenge.code2040.org/api/reverse", data = plainToken)
reversedString = reverseData.text[::-1]
reverseSubmit = {'token':token, 'string': reversedString}
requests.post("http://challenge.code2040.org/api/reverse/validate", data = reverseSubmit)

# Step 3
needleData = requests.post("http://challenge.code2040.org/api/haystack", data = plainToken)
needleMap = ast.literal_eval(needleData.text)
needleIndex = (needleMap['haystack'].index(needleMap['needle']))
needleSubmit = {'token':token, 'needle':needleIndex}
requests.post("http://challenge.code2040.org/api/haystack/validate", data = needleSubmit)

# Step 4
prefixData = requests.post("http://challenge.code2040.org/api/prefix", data = plainToken)
prefixMap = ast.literal_eval(prefixData.text)
prefixLength = len(prefixMap['prefix'])
solution = []
for x in prefixMap['array']:
	if x[:prefixLength] != prefixMap['prefix']:
	    solution.append(x)
prefixSubmit = {'token': token, 'array': solution}	    
requests.post("http://challenge.code2040.org/api/prefix/validate", json = prefixSubmit)