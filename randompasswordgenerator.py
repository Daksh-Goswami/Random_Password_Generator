## random  strong password generator :
from random import *
n=['0','1','2','3','4','5','6','7','8','9']
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
u=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
s=['!','@','#','$','%','^','&','*','<','>','?','.','/',';','~']
passkey=[]
pass1='a'
i=0
## logic to generate the password of variable length(as inputted by the user.)
def length():
    global i
    len=int(input('Please enter length of password you want in numerics.'))
    if len not in range(0,50):
        if len in ['!','@','#','$','%','^','&','*','(',')','{',']','}',']','|','<','>','/','?']:
            print('The password length cannot be a symbol.')
            length()
        elif len in l or len in u:
            print('The password cannot be a alphabet.')
            length()    
        else:
            print('This cannot be determined as a valid password length')
            length()
    elif len in range(0,50):
        if int(len)<5:
            print('The length of the password you want to set is too short \n Please specify a password length greater than 5.')
            length()
    i=int(len)
def randompasskey():
    global  i ,passkey
    while i>0:
        D=[l,s,u,n]        
        d=choice(D)
        p=choice(d)
        passkey.append(p)
        i=i-1
    for P in passkey:
        global pass1
        pass1=pass1+P
length()
randompasskey()        
password=pass1[1:len(pass1)] 
print(password)   