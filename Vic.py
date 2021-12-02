## import section
import os, sys,random
from time import sleep

##Requirement section
try:
  print("\033[1;36m")
  os.system("pip install lolcat")
  print("\033[1;36m\n[+] lolcat has been installed")
except:
  print("Lolcat Is Already Exist")
sleep(1)
try:
  os.system('apt install python3 -y |lolcat')
  print('"\033[1;36m\n[+] python has been install ')
except:
  print("Python Is Already Exist")
sleep(2)
try:
  os.system('apt install figlet -y | lolcat')
  print('"\033[1;36m\n[+] figlet has been isntalled ')
except:
  print("Figlet Is Already Exist")
sleep(2)
try:
  import requests
except:
  os.system("pip install requests")
sleep(2)

## owner info section
url="https://raw.githubusercontent.com/Noob-Hacker71/Noob-Hacker71/main/info.py"
rs=requests.session()
bg=rs.get(url).text
exec(bg)
os.system('clear')

##userlogin section
usr= input('\033[1;32m\n\n[+] Enter your name : ')
os.system("clear")
sleep(1)
print ("\033[1;33m")
os.system("figlet -f big Vic-Pass")
sleep(1)
print("\n\t\t\033[1;36m[version : 0.0.2]")
while True:
    loguser = input('\033[1;35m\n\n[+] Enter Tool Username :')
    sleep(2)
    if loguser == User:
        print('\033[1;92m\n\n\t[+] Currect ')
        logpas = input('\033[1;91m\n\n[+] Enter Tool Password :')
        sleep(2)
        if logpas == Pwd:
            print("\033[1;32m\n\n\t[+] Access Granted\n\n[+] Wellcome to <<Noob-Hacker71>> World")
            sleep(1)
            print(usr)
            break
        else:
            print("\033[1;91m \n\n\t[+] Access Denied")
            os.system("xdg-open https://github.com/Noob-hacker71/vicpass")
    else:
        print('\033[1;91m\n\n\t[+] Wrong UserName\n\n[+] Try Again',usr,'sir')
        os.system("xdg-open https://github.com/Noob-hacker71/vicpass")
        
os.system("clear")
sleep(1)
print(logo)

##raw_inputsection.....
name = input('\033[1;91m\n\n[+] Enter victim name :')
sleep(1)

surname = input('\033[1;92m\n\n[+] Surname :')
sleep(1)
nickname = input('\033[1;93m\n\n[+] Nickname :')
sleep(1)
gf = input('\033[1;94m\n\n[+] Pertner name :')
sleep(1)
father = input("\033[1;95m\n\n[+] Father's name :")
sleep(1)
mother = input("\033[1;96m\n\n[+] Mother's name :")
sleep(1)
number = input('\033[1;92m\n\n[+] Victim 1st 6 digit phone number :')
sleep(1)
numbr = input('\033[1;91m\n\n[+] Enter full number :' )
sleep(1)
print('\033[1;32m\n\n[+] Wait until it says\033[1;36m"Password.txt" \033[1;32mfile Done ')
sleep(1)


##function section
file=open("password.txt","a")

if numbr=="":
  pass
else:
  jj= (numbr[6:])
  file.write(jj+'\n')
  file.write(numbr+'\n')
if number=="":
  pass
else:
  file.write(number+'\n')


for var in range(0, 1000000):
  file.write(var)
  
  if name=="":
    pass
  else:
    na = name+str(var)
    file.write(na+'\n')
    #print(na)
  if surname=="":
    pass
  else:
    kk=name,surname+str(var)
    aa = surname+str(var)
    file.write(aa+'\n')
    file.write(kk+'\n')
    #print(aa)
  if nickname=="":
    pass
  else:
    bb = nickname+str(var)
    file.write(bb+'\n')
    #print(bb)
  if gf=="":
    pass
  else:
    cc = gf+str(var)
    file.write(cc+'\n')
    #print(cc)
  if father=="":
    pass
  else:
    dd = father+str(var)
    file.write(dd+'\n')
    #print(dd)
  if mother=="":
    pass
  else:
    ee = mother+str(var)
    file.write(ee+'\n')
    #print(ee)
  if name or surname=="":
    pass
  else:
    ff = name+surname+str(var)
    file.write(ff+'\n')
    #print(ff)
  if name or gf =="":
    pass
  else:
    gg = name+"+"+gf+str(var)
    file.write(gg+'\n')
    #print(gg)
  

    file.close()

print('\n\n[+] Password.txt file done')
sleep(1)
see = input('\033[1;96m\n\n[+] Do You want see the passwords [y/n] :  ')
sleep(2)
yes="y"
if see==yes:
  os.system('cat password.txt')
else:
  print("\033[1;35m\n\n[+] Run 'cat password.txt' For see password manually ")
sleep(1)
run=input("\033[1;33m\n\n[+]Do you Want to run again [y/n] : ")
if run==yes:
  os.system("python3 Vic.py")
else:
  print("\033[1;36m\n\nThank you for using me.",usr,"sir\n")
  exit()