#!/usr/bin/env python3
import webbrowser,os,sys,pyperclip
if(len(sys.argv))>1:
    address=' '.join(sys.argv[1:])
else:
    address=pyperclip.paste()
webbrowser.open("https://www.google.co.in/maps/place/"+address)

