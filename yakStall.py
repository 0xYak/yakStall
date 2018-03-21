#Installer for tools I use
#Made primarily because I'm really fucking indecisive about what OS to use on my box so I'm constantly reflashing it
#Edited and made for release because I thought somebody might get some use out of it 

import os
import sys





print("          _______  _______ ")
print("|\     /|(       )(  ____ \\")
print("( \   / )| () () || (    \/")
print(" \ (_) / | || || || (__    ")
print("  \   /  | |(_)| ||  __)   ")
print("   ) (   | |   | || (      ")
print("   | |   | )   ( || )      ")
print("   \_/   |/     \||/       ")
print("                           ")
print("Quick Installer Script")
print("FOLLOW ME ON TWITTER @0xYMF\n\n\n")


def menu():
	print("Main Menu: please select an option")
	print("[1] Install all tools")
	print("[2] View all tools and install individually")
	print("[0] Close this shit")
	lolz = input("Pick something: ")
	if lolz = "1":
		installz0rz()
	elif lolz = "2":
		listz0rz()
	elif lolz = "0":
		os.system("^C")
	else:
		print("Not an option fucker try something else")
		menu()
def installz0rz():
	os.system("sudo su")
	os.system("apt-get install nmap sqlmap gcc python-pip python3 git openssh-server openssh-client")
	pick2 = input("install lazyscript? [Y/n]")
	if pick2 = "y" or "Y":
		os.system("git clone https://github.com/arismelachroinos/lscript.git")
		os.system("cd lscript")
		os.system("chmod +x install.sh")
		os.system("bash install.sh")
	elif pick2 = "n" or "N":
		continue;
	pick3 = input("install anonurf?")
	if pick3 = "y" or "Y":
		os.system("git clone https://github.com/Und3rf10w/kali-anonsurf.git anonsurf")
		os.system("cd anonsurf")
		os.system("chmod +x installer.sh")
		os.system("bash installer.sh")
	elif pick3 = "n" or "N":
		continue;
	pick4 = input("Install WAScan? [Y/n]")
	if pick4 = "y" or "Y":
		os.system("git clone https://github.com/m4ll0k/WAScan.git wascan")
		os.system("cd wascan")
		os.system("pip install -r requirements.txt")
		print("Installation complete, use with 'python wascan.py'")

	else:
		print("invalid selection, retard, shutting down...")
def listz0rz():
	print("Select an option using its number")
	print("[1] nmap")
	print("[2] sqlmap")
	print("[3] Anonsurf")
	print("[4] gcc")
	print("[5] openssh")
	print("[6] anonsurf")

	












menu()