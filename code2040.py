import requests

token = input("Enter API Token")

register = {'token' : token, 'github': 'https://github.com/AllenDM/apichallenge'}


r = requests.post("http://challenge.code2040.org/api/register", data = register)

