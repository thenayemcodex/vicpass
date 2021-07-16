## import section

from time import sleep, time


##colore section

## owner info section
logo = '''▄▄    ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄    ▄▄   ▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄   ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   
█  █  █ █       █       █  ▄    █  █  █ █  █      █       █   █ █ █       █   ▄  █  
█   █▄█ █   ▄   █   ▄   █ █▄█   █  █  █▄█  █  ▄   █       █   █▄█ █    ▄▄▄█  █ █ █  
█       █  █ █  █  █ █  █       █  █       █ █▄█  █     ▄▄█      ▄█   █▄▄▄█   █▄▄█▄ 
█  ▄    █  █▄█  █  █▄█  █  ▄   █   █   ▄   █      █    █  █     █▄█    ▄▄▄█    ▄▄  █
█ █ █   █       █       █ █▄█   █  █  █ █  █  ▄   █    █▄▄█    ▄  █   █▄▄▄█   █  █ █
█▄█  █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█  █▄▄█ █▄▄█▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄█ █▄█▄▄▄▄▄▄▄█▄▄▄█  █▄█
'''
print('************************************************************************************************************************')

print(logo)

print('************************************************************************************************************************')
print('Owner: Tahsan Nayem')
print('Follow me : https://www.facebook.com/ntahsan.nayem')
print('************************************************************************************************************************')

##userlogin section
u = input('enter your name : ')

user = 'Tahsan Nayem'
upas = 'LOVE YOU THBD'
while True:
    loguser = input('Enter Tool Username :')
    if loguser == user:
        print('Currect User Name ')
        logpas = input('Enter Tool Password :')
        if logpas == upas:
            print("Currect Password.\nWellcome to Noob-Hacker World ")
            print(u)
            break
        else:
            print("Wrong Password")
    else:
        print('Wrong UserName.\nTry Again sir')
        print(u)
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

for var in range(0, 1000000):
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
