#   CODE 2040 API Challenge 
#   Author: AllenDM Allen Moody
import ast
import requests
import dateutil.parser
import dateutil.relativedelta

# Step 1
newFile = open('token.txt')
token = newFile.read()
token = token.rstrip()
register = {'token': token, 'github': 'https://github.com/AllenDM/apichallenge'}
requests.post("http://challenge.code2040.org/api/register", data=register)

# Step 2
plainToken = {'token': token}
reverseData = requests.post("http://challenge.code2040.org/api/reverse", data=plainToken)
reversedString = reverseData.text[::-1]
reverseSubmit = {'token':token, 'string': reversedString}
requests.post("http://challenge.code2040.org/api/reverse/validate", data=reverseSubmit)

# Step 3
needleData = requests.post("http://challenge.code2040.org/api/haystack", data=plainToken)
needleMap = ast.literal_eval(needleData.text)
needleIndex = (needleMap['haystack'].index(needleMap['needle']))
needleSubmit = {'token':token, 'needle':needleIndex}
requests.post("http://challenge.code2040.org/api/haystack/validate", data=needleSubmit)

# Step 4
prefixData = requests.post("http://challenge.code2040.org/api/prefix", data=plainToken)
prefixMap = ast.literal_eval(prefixData.text)
solution = []
for word in prefixMap['array']:
	if not word.startswith(prefixMap['prefix']):
	    solution.append(word)
prefixSubmit = {'token': token, 'array': solution}	    
requests.post("http://challenge.code2040.org/api/prefix/validate", json=prefixSubmit)

# Step 5
dateData = requests.post("http://challenge.code2040.org/api/dating", data=plainToken)
dateMap = ast.literal_eval(dateData.text)
dateStamp = dateutil.parser.parse(dateMap['datestamp'])
newDate = dateStamp + dateutil.relativedelta.relativedelta(seconds =+ dateMap['interval'])
newDate = newDate.isoformat()
newDateString = str(newDate)
if newDateString[19:] == "+00:00":
	newDateString = newDateString[:19] + "Z"
dateSolution = {'token': token, 'datestamp': newDateString}
requests.post("http://challenge.code2040.org/api/dating/validate", json=dateSolution)