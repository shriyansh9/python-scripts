#! python3
#searchIt.py - Google search using the text from the
# command line or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
	searchTerm = ' '.join(sys.argv[1:])
else:
	searchTerm = pyperclip.paste()


searchTerm = searchTerm.replace(' ','+')

webbrowser.open('https://www.google.co.in/search?q='+searchTerm)