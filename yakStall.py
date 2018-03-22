#Installer for tools I use
#Made primarily because I'm really fucking indecisive about what OS to use on my box so I'm constantly reflashing it
#Edited and made for release because I thought somebody might get some use out of it 

import os
import sys
from sys import platform





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

def operating():
	systm = sys.platform
	if systm == "win32":
		windows()
	elif systm == "linux" or "linux2":
		linux()
	elif systm == "darwin":
		osx()

def menu():
	print("Main Menu: please select an option")
	print("[1] Install all tools")
	print("[2] View all tools and install individually")
	print("[0] Close this shit")
	lolz = input("Pick something: ")
	if lolz == 1:
		installz0rz()
	elif lolz == 2:
		listz0rz()
	elif lolz == 0:
		os.system("[[^C")
	else:
		print("Not an option fucker try something else")
		menu()
def installz0rz():
	os.system("sudo su")
	os.system("apt-get install nmap sqlmap gcc python-pip python3 git openssh-server openssh-client")
	pick2 = input("install lazyscript? [Y/n]")
	if pick2 == "y" or "Y":
		os.system("git clone https://github.com/arismelachroinos/lscript.git")
		os.system("cd lscript")
		os.system("chmod +x install.sh")
		os.system("bash install.sh")
	elif pick2 == "n" or "N":
		pass
	pick3 = input("install anonurf?")
	if pick3 == "y" or "Y":
		os.system("git clone https://github.com/Und3rf10w/kali-anonsurf.git anonsurf")
		os.system("cd anonsurf")
		os.system("chmod +x installer.sh")
		os.system("bash installer.sh")
	elif pick3 == "n" or "N":
		pass
	pick4 = input("Install WAScan? [Y/n]")
	if pick4 == "y" or "Y":
		os.system("git clone https://github.com/m4ll0k/WAScan.git wascan")
		os.system("cd wascan")
		os.system("pip install -r requirements.txt")
		print("Installation complete, use with 'python wascan.py'")

	else:
		print("invalid selection, retard, shutting down...")
		menu()
def listz0rz():
	print("[1] nmap")
	print("[2] sqlmap")
	print("[3] Anonsurf")
	print("[4] gcc")
	print("[5] openssh")
	print("[6] hashcat")
	print("[7] WAScan")
	print("[8] WPScan")
	choice = input("Select an option using its number: ")
	if choice == 1:
		os.system("sudo apt-get install nmap")
		menu()
	elif choice == 2:
		os.system("sudo apt-get install sqlmap")
		menu()
	elif choice == 3:
		os.system("git clone https://github.com/Und3rf10w/kali-anonsurf.git anonsurf")
		os.system("cd anonsurf")
		os.system("chmod +x installer.sh")
		os.system("bash installer.sh")
		menu()
	elif choice == 4:
		os.system("sudo apt-get install gcc")
		menu()
	elif choice == 5:
		os.system("sudo apt-get install openssh=client && sudo apt-get install openssh-server")
		menu()
	elif choice == 6:
		os.system("git clone https://github.com/hashcat/hashcat.git")
		print("hashcat installed!")
		menu()
	elif choice == 7:
		os.system("git clone https://github.com/m4ll0k/WAScan.git wascan")
		os.system("cd wascan")
		os.system("pip install -r requirements.txt")
		print("WAScan installed, cd wascan and python wascan.py to use")
		menu()
	elif choice == 8:
		os.system("sudo apt-get install gcc git ruby ruby-dev libcurl4-openssl-dev make zlib1g-dev")
		os.system("git clone https://github.com/wpscanteam/wpscan.git wpscan")
		os.system("cd wpscan")
		os.system("sudo gem install bundler && bundle install --without test")
		menu()



	













menu()
