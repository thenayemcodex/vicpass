## import section
import os, sys

##Requirement section
os.system('apt install pyhton')
print('python has been install ')
os.system('apt install nano -y')
print('nano has been isntalled ')

## owner info section

os.system('clear')


print('\033[1;94m ***************************************************************************************************')

noob = ''' \033[1;91m ▄▄    ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄    \033[1;92m ▄▄   ▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄   ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   
\033[1;91m █  █  █ █       █       █  ▄    █  \033[1;92m █  █ █  █      █       █   █ █ █       █   ▄  █  
\033[1;91m █   █▄█ █   ▄   █   ▄   █ █▄█   █  \033[1;92m █  █▄█  █  ▄   █       █   █▄█ █    ▄▄▄█  █ █ █  
\033[1;91m █       █  █ █  █  █ █  █       █  \033[1;92m █       █ █▄█  █     ▄▄█      ▄█   █▄▄▄█   █▄▄█▄ 
\033[1;91m █  ▄    █  █▄█  █  █▄█  █  ▄   █   \033[1;92m █   ▄   █      █    █  █     █▄█    ▄▄▄█    ▄▄  █
\033[1;91m █ █ █   █       █       █ █▄█   █  \033[1;92m █  █ █  █  ▄   █    █▄▄█    ▄  █   █▄▄▄█   █  █ █
\033[1;91m █▄█  █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█  \033[1;92m █▄▄█ █▄▄█▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄█ █▄█▄▄▄▄▄▄▄█▄▄▄█  █▄█
'''
print (noob)


print('\033[1;92m NOOB-HACKER71.\nWe work to protect Bangladesh')

print('\033[1;94m ***************************************************************************************************')
print('\033[1;91m    Github : https://github.com/Noob-Hacker71')
print('\033[1;92m      Owner: Tahsan Nayem')
print('\033[1;92m Follow me : https://www.facebook.com/ntahsan.nayem')
print('\033[1;94m ***********************************************************************************************************')

##userlogin section
u = input('Enter your name : ')

user = 'Tahsan Nayem'
upas = 'THBD'
while True:
    loguser = input('\033[1;91m Enter Tool Username :')
    if loguser == user:
        print('\033[1;92m Currect User Name ')
        logpas = input('\033[1;91m Enter Tool Password :')
        if logpas == upas:
            print("\033[1;92m Currect Password.\nWellcome to Noob-Hacker World ")
            print(u)
            break
        else:
            print("\033[1;91m Wrong Password")
    else:
        print('\033[1;91m Wrong UserName.\nTry Again sir')
        print(u)
##raw_inputsection.....
name = input('\033[1;91m Enter victim name :')

surname = input('\033[1;92m Surname :')

nickname = input('\033[1;93m Nickname :')

gf = input('\033[1;94m Pertner name :')

father = input("\033[1;95m Mather's name :")

mother = input("\033[1;96m Mother's name :")

number = input('\033[1;92m Victim 1st 5 digit phone number :')
numbr = input('\033[1;91m Enter full number :' )
print(numbr[6:12])

show = 'yes'
showinput = input('Do you want to see the passwords : ')
if showinput == show
    print(na)
    print(aa)
    print(bb)
    print(cc)
    print(dd)
    print(ee)
    print(ff)
    print(gg)
    print(hh)
    print(jj)
else:
    print('password will shown in the password.txt file')

##function section

for var in range(0, 10000000):
    na = name+str(var)
    #print(na)
    aa = surname+str(var)
    #print(aa)
    bb = nickname+str(var)
    #print(bb)
    cc = gf+str(var)
    #print(cc)
    dd = father+str(var)
    #print(dd)
    ee = mother+str(var)
    #print(ee)
    ff = name+surname+str(var)
    #print(ff)
    gg = name+gf+str(var)
    #print(gg)
    hh = number+str(var)
    #print (hh)

    jj = numbr+str(var)
    #print (jj)

    file = open('password.txt', 'a')
    file.write(na+'\n')
    file.write(aa+'\n')
    file.write(bb+'\n')
    file.write(cc+'\n')
    file.write(dd+'\n')
    file.write(ee+'\n')
    file.write(ff+'\n')
    file.write(gg+'\n')
    file.write(hh+'\n')
    file.write(jj+'\n')
    file.close()
