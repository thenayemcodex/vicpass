## import section
from os import close,unlink
import os
import random
from types import new_class
##colore section
red = '\003[1;91m'
green = '\003[1;92m'
yellow = '\003[1;93m'
blue = '\003[1;94m'
purple = '\003[1;95m'
cyan = '\003[1;96m'
## owner info section
logo = '''\033[1;92m] ▄▄    ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄    ▄▄   ▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄   ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   
\033[1;92m]█  █  █ █       █       █  ▄    █  █  █ █  █      █       █   █ █ █       █   ▄  █  
\033[1;91m]█   █▄█ █   ▄   █   ▄   █ █▄█   █  █  █▄█  █  ▄   █       █   █▄█ █    ▄▄▄█  █ █ █  
\033[1;91m]█       █  █ █  █  █ █  █       █  █       █ █▄█  █     ▄▄█      ▄█   █▄▄▄█   █▄▄█▄ 
\033[1;91m]█  ▄    █  █▄█  █  █▄█  █  ▄   █   █   ▄   █      █    █  █     █▄█    ▄▄▄█    ▄▄  █
\033[1;92m]█ █ █   █       █       █ █▄█   █  █  █ █  █  ▄   █    █▄▄█    ▄  █   █▄▄▄█   █  █ █
\033[1;92m]█▄█  █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█  █▄▄█ █▄▄█▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄█ █▄█▄▄▄▄▄▄▄█▄▄▄█  █▄█
'''
print(logo)
print('\033[1;92m]Owner: Tahsan Nayem')
print('\033[1;91m]Follow me : https://www.facebook.com/ntahsan.nayem')


##userlogin section
user = 'Tahsan Nayem'
upas = 'LOVE YOU THBD'
while True:
    loguser = input('Enter Your Username :')
    if loguser == user:
        print('Currect User Name ')
        logpas = input('Enter Your Password :')
        if logpas == upas:
            print("Currect Password.\nWellcome to Noob-Hacker World ")
            break
        else:
            print("Wrong Password")
    else:
        print('Wrong UserName.\nTry Again sir')

##inputsection.....
name = input('Enter victim name :')

surname = input('surname :')

nickname = input('Nickname :')

gf = input('Pertner name :')

father = input("father's name :")

mother = input("mother's name :")

number = input('number :')
print(number[5:11])

##function section

for var in range(0, 20):
    na = name+str(var)
    print(na)
    aa = surname+str(var)
    print(aa)
    bb = nickname+str(var)
    print(bb)
    cc = gf+str(var)
    print(cc)
    dd = father+str(var)
    print(dd)
    ee = mother+str(var)
    print(ee)

    all = (na,aa,bb,cc,dd,ee)
    pas = (all)

    file = open('password.txt','a')
    file.write(str(all))
    file.close()
