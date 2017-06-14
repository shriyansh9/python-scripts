#! python3
#mapIt.py - Launches a map using the address from the
# command line or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()

address = address.replace(',',' ')
address = address.replace(' ','+')

webbrowser.open('https://www.google.com/maps/place/'+address)