## import section
import os, sys
from time import sleep

##Requirement section
try:
  import python3
except:
  print("\033[1;33m")
  os.system('apt install python3 -y')
  print('python has been install ')
  sleep(2)
try:
  import figlet
except:
  print("\033[1;34m")
  os.system('apt install figlet -y')
  print('figlet has been isntalled ')
  sleep(2)

## owner info section

os.system('clear')

##userlogin section
usr= input('\033[1;32m\n\n[+] Enter your name : ')
sleep(1)
print ("\033[1;33m")
os.system("figlet -f big Vic-Pass")
sleep(1)
while True:
    loguser = input('\033[1;35m\n\n[+] Enter Tool Username :')
    sleep(2)
    if loguser == "NOOB-HACKER71":
        print('\033[1;92m\n\n\t[+] Currect ')
        logpas = input('\033[1;91m\n\n[+] Enter Tool Password :')
        sleep(2)
        if logpas == "THBD":
            print("\033[1;32m\n\n\t[+] Access Granted\n\n[+] Wellcome to <<Noob-Hacker71>> World")
            sleep(1)
            print(usr)
            break
        else:
            print("\033[1;91m \n\n\t[+] Access Denied")
    else:
        print('\033[1;91m\n\n\t[+] Wrong UserName\n\n[+] Try Again',usr,'sir')
        
os.system("clear")
sleep(1)
print('\033[1;94m *********************************************************************')
sleep(1)
noob = '''
\033[1;92m     __            _          \033[1;92m                  _           \033[1;91m _____ _ 
\033[1;92m  /\ \ \___   ___ | |__       \033[1;92m  /\  /\__ _  ___| | _____ _ _\033[1;91m|___  / |
\033[1;92m /  \/ / _ \ / _ \| '_ \ \033[1;91m_____\033[1;92m / /_/ / _` |/ __| |/ / _ \ '__|\033[1;91m / /| |
\033[1;92m/ /\  / (_) | (_) | |_) |\033[1;91m_____\033[1;92m/ __  / (_| | (__|   <  __/ |   \033[1;91m/ / | |
\033[1;92m\_\ \/ \___/ \___/|_.__/      \033[1;92m\/ /_/ \__,_|\___|_|\_\___|_| \033[1;91m /_/  |_|
'''
print (noob)
sleep(1)

print("\033[1;94m\n[+] Termux Hacker BD {THBD}")
sleep(1)
print("\033[1;33m\n[+] We work to protect Bangladesh")
sleep(1)
print('\033[1;94m\n *********************************************************************')
sleep(1)
print('\033[1;92m[+] Author : Tahsan Nayem')
sleep(1)
print('\033[1;92m\n[+] Follow me : https://www.facebook.com/ntahsan.nayem')
sleep(1)
print('\033[1;94m**********************************************************************')

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


for var in range(0, 100):
  
  if name=="":
    pass
  else:
    na = name+str(var)
    file.write(na+'\n')
    #print(na)
  if surname=="":
    pass
  else:
    kk=name+surname+str(var)
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
    gg = name+gf+str(var)
    file.write(gg+'\n')
    #print(gg)


    file.close()
print('\n\n[+] Password.txt file done')
sleep(1)
see = input('\033[1;95m\n\n[+] Do You want see the passwords [y/n] :  ')
sleep(2)
y="y"
if see==y:
  os.system('cat password.txt')
else:
  print("\033[1;35m\n\n[+] Run 'cat password.txt' For see password manually ")
sleep(1)
run=input("\033[1;33m\n\n[+]Do you Want to run again [y/n] : ")
if run==y:
  os.system("python3 Task.py")
else:
  print("\033[1;36m\n\nThank you for using me.",usr,"sir")
  exit()