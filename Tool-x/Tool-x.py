import os 
import time
def toolx():
	print("""$$$$$$$$\                  $$\                     $$\   $$\ 
\__$$  __|                 $$ |                    $$ |  $$ |
   $$ | $$$$$$\   $$$$$$\  $$ |                    \$$\ $$  |
   $$ |$$  __$$\ $$  __$$\ $$ |      $$$$$$\        \$$$$  / 
   $$ |$$ /  $$ |$$ /  $$ |$$ |      \______|       $$  $$<  
   $$ |$$ |  $$ |$$ |  $$ |$$ |                    $$  /\$$\ 
   $$ |\$$$$$$  |\$$$$$$  |$$ |                    $$ /  $$ |
   \__| \______/  \______/ \__|                    \__|  \__|
                """)
	print("\n")
	mainmenu()

def mainmenu():
	print("""
	Tool available:
	1.Local Machine Scanning
	2.Jarvis site scanning
	3.Web Server Scanning
	4.Web Application scanning
	5.scammer
	6.Port scanning
	7.Upgrade Your linux system
	8.update your linux system
	9.Tool-x
	10.exit
	""")
	main()

def Lynis():
	os.system("cd lynis; sudo ./lynis audit system; cd ..")
	os.system("mousepad $HOME/scanningreport.log")
	os.system("cd ..")
	aconf()
def sqlmap():
	url=input("Enter Your Target Ip or Url(https://example.com): ")
	os.system("cd sqlmap; python3 sqlmap.py -u " + url)
	os.system("cd ..")
	aconf()

def nikto():
	url=input("Enter your Target Ip or url(https://Example.com): ")
	os.system("cd nikto/program; sudo ./nikto.pl -h " + url )
	os.system("cd ..")
	aconf()

def uniscan():
	url=input("Enter Your Target Ip or Url(http://www.example.com/): ")
	os.system("cd uniscan; perl uniscan.pl -u "+ url + " -qweds; cd ..")
	aconf()

def skipfish():
	fname=input("Enter file name(don't repeat the file name): ")
	ip=input("Enter the target Ip: ")
	os.system("cd skipfish; sudo skipfish -o " + fname +" " + ip)
	os.system("cd ..")
	aconf()
def port():
	IP = input("[+]Enter the target IP: ")
	M="nmap "+ IP
	os.system(M)
	aconf()
def scan():
	url=input("Enter Your Target Ip or Url(http://www.example.com/): ")
	os.system("cd uniscan; perl uniscan.pl -u "+ url + " -qweds; cd ..")
	url=input("Enter your Target Ip or url(https://Example.com): ")
	os.system("cd nikto/program; sudo ./nikto.pl -h " + url )
	os.system("cd ..")
	os.system("cd lynis; sudo ./lynis audit system; cd ..")
	os.system("mousepad $HOME/scanningreport.log")
	os.system("cd ..")
	url=input("Enter Your Target Ip or Url(https://example.com): ")
	os.system("cd sqlmap; python3 sqlmap.py -u " + url)
	os.system("cd ..")
	IP = input("[+]Enter the target IP: ")
	M="nmap "+ IP
	os.system(M)
	fname=input("Enter file name(don't repeat the file name): ")
	ip=input("Enter the target Ip: ")
	os.system("cd skipfish; sudo skipfish -o " + fname +" " + ip)
	os.system("cd ..")
	aconf()
	
	

def update():
	os.system("sudo apt update")
	os.system("apt list --upgradable")
	aconf()

def upgrade():
	print("")
	print("")
	a=input("Do you want to upgrade the above mentioned Packages?(Y/N):")  
	if a=="Y" or a == "y":
	    #os.system('clear')
	    os.system("sudo apt autoremove")
	    os.system("sudo apt full-upgrade -y")
	    print("****************************************")
	    print("")
	    print("Your System is Succussfully upgraded....")
	    print("")
	    print("****************************************")
	elif a=="N" or a=="n":
	    mainmenu()
	else:
	    print("Enter the Valid Input")
	    upgrade() 
	
def aconf():
	print("")
	print("")
	loop = input("[+]Do you want to continue with this Tool? (Y/N) ")

	if loop=="Y" or loop == "y":
		toolx()

	elif loop=="N" or loop == "n":
	    print("****************************************")
	    print("")
	    print("           Thank you for using Tool - X....!")
	    print("")
	    print("****************************************")
	else:
	    print("Enter the Valid Input")
	    aconf()

def main():
	inp=input("Enter the valid Number:")
	if inp=="1":
		Lynis()
	elif inp=="2":
		uniscan()
	elif inp=="3":
		nikto()
	elif inp=="4":
		sqlmap()
	elif inp=="5":
		skipfish()
	elif inp=="6":
	    	port()
	elif inp=="7":
		upgrade()
	elif inp=="8":
		update()
	elif inp=="9":
		scan()
		
	elif inp=="10":
	    print("***********************************************")
	    print("")
	    print("Quiting... ThankYou for Using our TOOL - X...!")
	    print("")
	    print("***********************************************")
	    quit()
	else:
		print("Invalid Input")
		main()
toolx()


