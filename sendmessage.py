#! python3
# sendmessage.py - takes message and phone no. as input and
# sends a text message to that phone no.
# textbelt key is used to send sample text, for customized message purchase own key.
# https://textbelt.com/
import requests

message = input('Enter message: ')
phone = input('Enter phone no. (with country code e.g. +91 for India): ')

payload = {'phone': phone, 'message': message, 'key': 'textbelt'}

r = requests.post("http://textbelt.com/text",data=payload)

if r.json()['success']:
	print ('Success! :)')
else:
	print ('Error :(')