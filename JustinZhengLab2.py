##########################
# CIS 117 Python Programming:  Lab #2
#
# Programming with Loops and Functions 
#
##########################

import re
def passwordvalidate(): 
    while True:
        password = input ('Enter Your Password: ')
        passwordcheck = input ('Re-enter Your Password: ')
        ReqPasswordLength = 8 
        print (password)
        if len(password) < ReqPasswordLength:
            print ('Your password must be longer than or equal to 8 characters!')
        elif password != passwordcheck:
            print ('Your password does not match!')  
        elif re.search('[0-9]',password) is None:
            print ('Your password requires a digit!')    
        elif re.search ('[A-Z]', password) is None:
            print ('Your password requires a capital letter!')
        else:
            print ('Your password is fine!')
            break
passwordvalidate()

##########################
#Run
#
#Enter Your Password: password
#Re-enter Your Password: password
#Your password must be longer than 8 characters!
#Enter Your Password: passwords
#Re-enter Your Password: passwords
#Your pass word requires a digit!
#Enter Your Password: passwords1
#Re-enter Your Password: passwords
#Your password does not match!
#Enter Your Password: passwords1
#Re-enter Your Password: passwords1
#Enter Your Password: Passwords1
#Re-enter Your Password: Passwords1
#Your password is fine!
##########################




    