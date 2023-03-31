#-------------------{ADMIN INFO}------------------------
# DEVELOPER  : FARHAN KHAN 
# TEAM       : COBRA 404 CYBER
# WHATSAPP   : +8801838847447
# FACEBOOK   : https://www.facebook.com/F4RH4NKHAN
# SECURED BY : FARHAN KHAN 
#------------------------------------------------------
import os,time
try:
  import requests
except:
  print("\033[5m[\033[38;5;46m✓\033[5m]\033[38;5;46m Installing missing modules.... ")
  time.sleep(1)
  os.system("pip install requests")
  os.system("pkg install figlet")

import os
import sys
import time
import requests 
import random
#import your dady Farhan 🙂
os.system("clear")
try:
  os.system("mkdir /sdcard/T-MAKER")
  os.system("mkdir /data/data/com.termux/files/usr/etc/.propertys")
except:
  pass
os.system("clear")
logo=("""\033[38;5;46m

████████     ███    ███  █████  ██   ██ ███████ ██████  
   ██        ████  ████ ██   ██ ██  ██  ██      ██   ██ 
   ██   ███  ██ ████ ██ ███████ █████   █████   ██████  
   ██        ██  ██  ██ ██   ██ ██  ██  ██      ██   ██ 
   ██        ██      ██ ██   ██ ██   ██ ███████ ██   ██ 
                                        \033[1;37m
×××××××××××××××××××××××××××××××××××××××××××××××××××××××××
\033[1;37m❲\033[38;5;46m+\033[1;37m❳ DEVELOPER : FARHAN KHAN
\033[1;37m❲\033[38;5;46m+\033[1;37m❳ GITHUB    : COBRA-404-CYBER
\033[1;37m❲\033[38;5;46m+\033[1;37m❳ TEAM      : COBRA 404 CYBER
\033[1;37m❲\033[38;5;46m+\033[1;37m❳ VERSION   : 1.5
\033[1;37m❲\033[38;5;46m+\033[1;37m❳ PROJECT   : T-MAKER
\033[1;37m❲\033[38;5;46m+\033[1;37m❳ FACEBOOK  : @F4RH4NKHAN
×××××××××××××××××××××××××××××××××××××××××××××××××××××××××""")
def clear():
  os.system("clear")
  print(logo)
def line():
  print("\033[1;37m×××××××××××××××××××××××××××××××××××××××××××××××××××××××××")


def slw (X):
  for i in X:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.1)

def old():
  clear()
  nam = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER YOUR NAME : ")
  STNM = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] SHORT NAME FOR BANER : ")
  FB = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER YOUR FB ID NAME : ")
  FBLINK = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER FB ID LINK : ")
  GTHBLNK = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER GITHUB USERNAME : ")
  OUTPUT = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER YOUR OUTPUT FILE NAME : ")
  os.system("git clone https://github.com/FRAHN-KHAN/2009 ; cd 2009 ; mv old.txt .. ; cd .. ; rm -rf 2009")
  f="old.txt"
  file = open(f,"r")
  code = file.read()
  cod = code.replace("EXAMPLE_NAME",nam)
  co = cod.replace("EXAMPLE_FB_ID_LINK",FBLINK)
  c = co.replace("EXAMPLE_GITHUB",GTHBLNK).replace("SHRT_NM",STNM).replace("EXAMPLE_FB",FB)
  out = OUTPUT
  bal = open(out,"w")
  bal.write(c)
  os.system(f"mv {out} /sdcard/T-MAKER")
  os.system("rm old.txt")
  clear()
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] YOUR TOOLS SAVED TO T-MAKER IN YOU SDCARD")
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] TnQ FOR USING YOUR TOOL BEST OF LUCK ")
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] TOOL TA ENCRYPT KORE NIYEN UPLOAD DEWAR AGE")
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] AMADER GITHUB THEKE CODE-X TOOL DIYE ENCRYPT KORIYEN")
  line()
  bkcd=input("DO YOU KNOW WHAT TO DO NEXT ? (y/n) ")
  bkcd = bkcd.replace(" ","")
  if bkcd in ["n","N"]:
    os.system("xdg-open https://fb.watch/jthVaXFsdI/")
  elif bkcd in ["Y","y"]:
    pass
  else:
    pass
  sys.exit()

def clone():
  clear()
  nam = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER YOUR NAME : ")
  STNM = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] SHORT NAME FOR BANER : ")
  FB = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER YOUR FB ID NAME : ")
  FBLINK = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER FB ID LINK : ")
  GTHBLNK = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER GITHUB USERNAME : ")
  OUTPUT = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER YOUR OUTPUT FILE NAME : ")
  os.system("git clone https://github.com/FRAHN-KHAN/RANDOM ; cd RANDOM ; mv cln.txt .. ; cd .. ; rm -rf RANDOM")
  f="cln.txt"
  file = open(f,"r")
  code = file.read()
  cod = code.replace("EXAMPLE_NAME",nam)
  co = cod.replace("EXAMPLE_FB_ID_LINK",FBLINK)
  c = co.replace("GITHUB_KINK",GTHBLNK).replace("SHORT_NAME",STNM).replace("FB_ID_NAME",FB)
  out = OUTPUT
  bal = open(out,"w")
  bal.write(c)
  os.system(f"mv {out} /sdcard/T-MAKER")
  os.system("rm cln.txt")
  clear()
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] YOUR TOOLS SAVED TO T-MAKER IN YOU SDCARD")
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] TnQ FOR USING YOUR TOOL BEST OF LUCK ")
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] TOOL TA ENCRYPT KORE NIYEN UPLOAD DEWAR AGE")
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] AMADER GITHUB THEKE CODE-X TOOL DIYE ENCRYPT KORIYEN")
  line()
  bkcd=input("DO YOU KNOW WHAT TO DO NEXT ? (y/n) ")
  bkcd = bkcd.replace(" ","")
  if bkcd in ["n","N"]:
    os.system("xdg-open https://fb.watch/jthVaXFsdI/")
  elif bkcd in ["Y","y"]:
    pass
  else:
    pass
  sys.exit()

def sms():
  clear()
  nam = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER YOUR NAME : ")
  STNM = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] SHORT NAME FOR BANER : ")
  FB = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER YOUR FB ID NAME : ")
  FBLINK = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER FB ID LINK : ")
  GTHBLNK = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER GITHUB USERNAME : ")
  OUTPUT = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER YOUR OUTPUT FILE NAME : ")
  os.system("git clone https://github.com/FRAHN-KHAN/SMS-bomber ; cd SMS-bomber ; mv sms.txt .. ; cd .. ; rm -rf SMS-bomber")
  f="sms.txt"
  file = open(f,"r")
  code = file.read()
  cod = code.replace("EXAMPLE-USER-NAME",nam)
  co = cod.replace("EXAMPLE-FB-ID-LINK",FBLINK)
  c = co.replace("EXAMPLE-GITHUB-LINK",GTHBLNK).replace("SHORT_NAME",STNM).replace("XXXXXX",FB)
  out = OUTPUT
  bal = open(out,"w")
  bal.write(c)
  os.system(f"mv {out} /sdcard/T-MAKER")
  os.system("rm sms.txt")
  clear()
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] YOUR TOOLS SAVED TO T-MAKER IN YOU SDCARD")
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] TnQ FOR USING YOUR TOOL BEST OF LUCK ")
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] TOOL TA ENCRYPT KORE NIYEN UPLOAD DEWAR AGE")
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] AMADER GITHUB THEKE CODE-X TOOL DIYE ENCRYPT KORIYEN")
  line()
  bkcd=input("DO YOU KNOW WHAT TO DO NEXT ? (y/n) ")
  bkcd = bkcd.replace(" ","")
  if bkcd in ["n","N"]:
    os.system("xdg-open https://fb.watch/jthVaXFsdI/")
  elif bkcd in ["Y","y"]:
    pass
  else:
    pass
  sys.exit()

def gf():
  clear()
  nam = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER YOUR NAME : ")
  STNM = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] SHORT NAME FOR BANER : ")
  FB = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER YOUR FB ID NAME : ")
  FBLINK = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER FB ID LINK : ")
  GTHBLNK = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER GITHUB USERNAME : ")
  OUTPUT = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER YOUR OUTPUT FILE NAME : ")
  f="gfhak.txt"
  file = open(f,"r")
  code = file.read()
  cod = code.replace("EXAMPLE_NAME",nam)
  co = cod.replace("EXAMPLE_FB_ID_LINK",FBLINK)
  c = co.replace("GITHUB_KINK",GTHBLNK).replace("SHORT_NAME",STNM).replace("FB_ID_NAME",FB)
  out = OUTPUT
  bal = open(out,"w")
  bal.write(c)
  os.system(f"mv {out} /sdcard/T-MAKER")
  clear()
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] YOUR TOOLS SAVED TO T-MAKER IN YOU SDCARD")
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] TnQ FOR USING YOUR TOOL BEST OF LUCK ")
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] TOOL TA ENCRYPT KORE NIYEN UPLOAD DEWAR AGE")
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] AMADER GITHUB THEKE CODE-X TOOL DIYE ENCRYPT KORIYEN")
  line()
  bkcd=input("DO YOU KNOW WHAT TO DO NEXT ? (y/n) ")
  bkcd = bkcd.replace(" ","")
  if bkcd in ["n","N"]:
    os.system("xdg-open https://fb.watch/jthVaXFsdI/")
  elif bkcd in ["Y","y"]:
    pass
  else:
    pass
  sys.exit()

def setup():
  clear()
  nam = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER YOUR NAME : ")
  STNM = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] SHORT NAME FOR BANER : ")
  FB = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER YOUR FB ID NAME : ")
  FBLINK = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER FB ID LINK : ")
  GTHBLNK = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER GITHUB USERNAME : ")
  OUTPUT = input("\n\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER YOUR OUTPUT FILE NAME : ")
  f="stp.py"
  file = open(f,"r")
  code = file.read()
  cod = code.replace("EXAMPLE_NAME",nam)
  co = cod.replace("EXAMPLE_FB_ID_LINK",FBLINK)
  c = co.replace("GITHUB_KINK",GTHBLNK).replace("SHORT_NAME",STNM).replace("FB_ID_NAME",FB)
  out = OUTPUT
  bal = open(out,"w")
  bal.write(c)
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] YOUR TOOLS SAVED TO T-MAKER IN YOU SDCARD")
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] TnQ FOR USING YOUR TOOL BEST OF LUCK ")
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] TOOL TA ENCRYPT KORE NIYEN UPLOAD DEWAR AGE")
  print("\033[1;37m[\033[38;5;46m+\033[1;37m] AMADER GITHUB THEKE CODE-X TOOL DIYE ENCRYPT KORIYEN")
  line()
  os.system(f"mv {out} /sdcard/T-MAKER")
  bkcd=input("DO YOU KNOW WHAT TO DO NEXT ? (y/n) ")
  bkcd = bkcd.replace(" ","")
  if bkcd in ["n","N"]:
    os.system("xdg-open https://fb.watch/jthVaXFsdI/")
  elif bkcd in ["Y","y"]:
    pass
  else:
    pass
  sys.exit()





#-------------{ MEMU }------------
clear()
slw("\033[38;5;46mWELCOME TO T-MAKER PROJECT BY COBRA 404 CYBER")
time.sleep(1)
clear()

ki = ""
lat = "QWERTYUIOPASDFGHJKLZXCVBNM0987654321"
for i in range(20):
  ki+=random.choice(lat)
try:
  file=open("/data/data/com.termux/files/usr/bin/.BYPASS_ER_MYRE_CUDI-_-","r")
  key=file.read()
  file.close()
except FileNotFoundError:
  file=open("/data/data/com.termux/files/usr/bin/.BYPASS_ER_MYRE_CUDI-_-","w")
  file.write(ki)
  file.close()
uid = os.getuid()
key1 = open("/data/data/com.termux/files/usr/bin/.BYPASS_ER_MYRE_CUDI-_-","r").read()
papa = (f"C4C{key1}88{uid}FK==")
lok=requests.get("https://raw.githubusercontent.com/FARHAN-KHAN998/papa/main/Bypass_er_myre_cudi.txt").text
if papa in lok:
  print("\033[0m[\033[38;5;46m+\033[0m]\033[38;5;46m CONGRATULATION YOU KEY IS APPROVED ")
  time.sleep(1)
  pass
else:
  print("\033[1;37m×××××××××××××××××××××××××××××××××××××××××××××××××××××××××")
  print("                    \033[38;5;195m ★\033[38;5;196m NOTICE \033[38;5;195m★\n                    ------------\n \n<> Assalamu alaikum <> Apni jodi tool tar aproval can\ntahole amader public group a 300 membar invite kore setar\nprof screen video kore amader page a diben obossoi\namader group er screen video soho.. \033[38;5;46mTnQ 感謝 \033[0m")
  print("\033[1;37m×××××××××××××××××××××××××××××××××××××××××××××××××××××××××")
  print("\033[0m[\033[38;5;46m+\033[0m] YOUR KEY : \033[38;5;46m"+papa+"\033[0m")
  print("×××××××××××××××××××××××××××××××××××××××××××××××××××××××××")
  input("\033[1;37m[\033[38;5;46m+\033[1;37m] ENTER TO FIND OUR PAGE ")
  os.system("xdg-open https://www.facebook.com/Cobra.404.Cyber/")
  print("\n\033[0m[\033[38;5;46m+\033[0m]\x1b[38;5;208m NOW JUST WAITE FOR APPROVAL\n")
  sys.exit()


def lvseha():
  clear()
  print("[01] START TOOL MAKING FOR YOUR OWN ")
  print("[02] JOIN OUR PUBLIC GROUP FOR SUPPORT")
  print("[03] FOLLOW OUR PAGE FOR MORE TOOLS")
  print("[04] CONTACT THE DEVELOPER ON FACEBOOK ")
  print("[05] DON'T KNOW HOW TO USE")
  print("[00] EXIT")
  line()
  usr = input("\033[1;37m[\033[38;5;46m+\033[1;37m] YOUR CHOICE : ")
  usr = usr.replace(" ","")
  if usr in ["1","01"]:
    clear()
    print("[01] MAKE YOUR OWN RANDOM CLONING TOOL")
    print("[02] MAKE YOUR OWN 2009-2013 CLONING TOOL")
    print("[03] MAKE YOU OWN BD SMS BOMBING TOOL")
    print("[04] MAKE A GF/BF HACK TOOL")
    print("[05] MAKE YOUR OWN TERMUX SETUP TOOL")
    line()
    ica = input("\033[1;37m[\033[38;5;46m+\033[1;37m] YOUR CHOICE : ")
    ica = ica.replace(" ","")
    if ica == "1" or ica == "01":
      clone()
    elif ica == "2" or ica == "02":
      old()
    elif ica == "3" or ica == "03":
      sms()
    elif ica == "4" or ica == "04":
      gf()
    elif ica == "5" or ica == "05":
      setup()
    else:
      print("\033[1;37m\n[\033[1;31m!\033[1;37m]\033[1;31m WRONG OPTION ENTERED..\n")
      time.sleep(1)
      lvseha()
  elif usr in ["2","02"]:
    os.system("xdg-open https://www.facebook.com/groups/1354738058401296/?ref=share&mibextid=NSMWB")
    lvseha()
  elif usr in ["3","03"]:
    os.system("xdg-open https://www.facebook.com/Cobra.404.Cyber/")
    lvseha()
  elif usr in ["4","04"]:
    os.system("xdg-open https://www.facebook.com/FarhanXTermux?mibextid=ZbWKwL")
    lvseha()
  elif usr == "5" or usr == "05":
    os.system("xdg-open https://www.facebook.com/F4RH4NKHAN/videos/1180433836004244/?idorvanity=1354738058401296&mibextid=Nif5oz")
    lvseha()
  elif usr in ["0","00"]:
    print("\nTNX FOR USE 😊")
    os.system("xdg-open https://www.facebook.com/Cobra.404.Cyber/")
    sys.exit()
  else:
    print("\033[1;37m\n[\033[1;31m!\033[1;37m]\033[1;31m WRONG OPTION ENTERED..\n")
    time.sleep(1)
    lvseha()


lvseha()