import os
import pyfiglet

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()

def textDecoration():
	print('-----------------------------------------------------------')
	ascii_banner = pyfiglet.figlet_format("Magic Cards")
	print(ascii_banner)
	print("V. 1.0")