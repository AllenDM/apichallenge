#   CODE 2040 API Challenge
#   
#   Author: AllenDM Allen Moody

import requests


token = input("Enter API Token: ")

# Step 1
register = {'token' : token, 'github': 'https://github.com/AllenDM/apichallenge'}

requests.post("http://challenge.code2040.org/api/register", data = register)

# Step 2
reverseRegister = {'token': token}

r = requests.post("http://challenge.code2040.org/api/reverse", data = reverseRegister)

reversedString = r.text[::-1]

reverseSolution = {'token': token, 'string': reversedString}

requests.post("http://challenge.code2040.org/api/reverse/validate", data = reverseSolution)
