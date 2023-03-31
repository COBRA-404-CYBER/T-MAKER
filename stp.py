import os
import sys
import time


# FB_ID_NAME
# EXAMPLE_FB_ID_LINK
# GITHUB_KINK
# SHORT_NAME
# EXAMPLE_NAME

os.system("xdg-open https://www.facebook.com/groups/1354738058401296/?ref=share&mibextid=NSMWB")

def line():
  print("------------------------------------------------------")

def clear():
  os.system("clear")
  baner= os.system("figlet -f slant SHORT_NAME")
  baner = str(baner)
  baner = baner.replace("0","")
  print(baner)
  line()
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] AUTHOR   : EXAMPLE_NAME ")
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] GITHUB   : GITHUB_KINK ")
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] PROJECT  : TERMUX SETUP ")
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] FACEBOOK : FB_ID_NAME ")
  line()
  
def basic():
  os.system("apt update")
  os.system("apt upgrade")
  os.system("pkg install nano")
  os.system("gem install lolcat")
  os.system("pkg install ruby")
  os.system("pip install requests")
  os.system("pip install mechanize")
  os.system("pip install bs4")
  os.system("pip install features")
  os.system("pip install futures")
  clear()
  print("YOUR TERMUX IS READY TO USE ")
def full():
  os.system("apt update")
  os.system("apt upgrade")
  os.system("pkg install nano")
  os.system("gem install lolcat")
  os.system("pkg install ruby")
  os.system("pip install requests")
  os.system("pip install mechanize")
  os.system("pip install bs4")
  os.system("pip install features")
  os.system("pip install futures")
  os.system("pip2 install mechanize")
  os.system("pip2 install requests")
  os.system("pip2 install bs4")
  os.system("pkg install python2")
  os.system("apt install tmux")
  os.system("pkg install curl")
  os.system("pkg install toilet")
  os.system("pkg install cowsay")
  os.system("pkg install figlet")
  os.system("pkg install awesomeshot")
  os.system("pkg install inotify-tools")
  os.system("pkg install clang")
  os.system("pkg install bat")
  os.system("pkg install imagemagick")
  os.system("pkg install exa")
  os.system("pkg install lf")
  os.system("pkg install mpd")
  os.system("pkg install neovim")
  os.system("pkg install openssh")
  os.system("pkg install neofetch")
  os.system("pkg install termux-api")
  os.system("pkg install tmux")
  os.system("pkg install zsh")
  os.system("pkg i -y git bc")
  clear()
  print("YOUR TERMUX IS READY TO USE")





clear()
print("[01] TERMUX BASIC SETUP")
print("[02] TERMUX FULL SETUP")
print("[03] CONTACT ME ON FACEBOOK ")
line()
usr = input("[+] YOUE CHOICE : ")
usr = usr.replace(" ","")
if usr in ["1","01"]:
  basic()
elif usr in ["2","02"]:
  full()
elif usr in ["03","3"]:
  os.system("xdg-open EXAMPLE_FB_ID_LINK")
else:
  print("\n [!] WRONG OPTION ENTERED...")
  sys.exit()
