
#import
import os  , time
from time import sleep
#color
GREEN = '\x1b[38;5;46m'
RED = '\x1b[38;5;196m'
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK = "\033[1;30m"



logo = ('''

\x1b[38;5;46m              █░█ █ ▀█▀ █░░ ▄▀█ █▀█
\033[1;33m              █▀█ █ ░█░ █▄▄ █▀█ █▀▄ ''')

name = ('''\033[1;93m ╔═════════════════[\033[1;32m 𝘼𝘿𝙈𝙄𝙉 \033[1;32m]═════════════════╗
 \033[1;93m║    \033[1;96m[✓] CREATED BY\33[0;m   : \033[1;96m HITLAR VAI    \033[1;32m     ║
 \033[1;93m║    \033[1;36m[✓] TOOL STATUS  : \033[1;36m TERMUX SETUP     \033[1;32m  ║\033[1;93m ᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈─╌❊❊╌──┈⊰᯽
\033[1;93m ╚═══════════════[\033[1;93m HITLAR VAI \033[1;32m]══════════════╝''')

menu = ('''\033[1;96m
 [1] Basic setup
 [2] Join us
 [3] Contact me
 [4] Exit ''')


def setup():
	os.system("clear")
	print(f'''\x1b[38;5;196m          ╔════════════════════════╗
      \x1b[38;5;196m    ║\x1b[38;5;46m........Starting........\x1b[38;5;196m║
       \x1b[38;5;196m   ╚════════════════════════╝ {YELLOW}''')
	print("")
	time.sleep(2)
	os.system("pkg update -y && pkg upgrade -y && pkg install git -y &&pkg install python -y && pkg install python2 -y && pkg install python3 -y && pkg install curl -y && pkg install wget -y && pip install requests  mechanize bs4")
	
def join():
	os.system("xdg-open https://facebook.com/groups/332342964206367")
	
def contact():
	os.system("xdg-open https://www.facebook.com/profile.php?id=100069950807873")
	
def Exit():
	os.system("exit")
	os.system("clear")

def main():
	os.system("loading")
	time.sleep(3)
	os.system("clear")
	print(logo)
	print("")
	print(name)
	print("")
	print('\033[1;93m ×××××××××××××××××××××××××××××××××××××××××××××')
	print(menu)
	print("")
	print('\x1b[38;5;46m××××××××××××××××××××××××××××××××××××××××××××××')
	option=input(f"{RED}Select a Option: {YELLOW}")
	if option =='1':
		setup()
	elif option =='2':
		join()
		main()
	elif option =='3':
		contact()
		main()
	elif option =='4':
		print("")
		print("           ........Okey Bye........")
		time.sleep(2)
		Exit()
	else:
		print("")
		print("   ....Oh  dear. You choose wrong option....")
		time.sleep(3)
		main()
		
	
main()

