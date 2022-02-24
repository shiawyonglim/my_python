import re

from sqlalchemy import false
print('password msut contain 8-20 Letters( Uppercase , Lowercase )and Number')
password = input('enter your password:')
print()
factor = True

while factor == True:
    if (len(password)) >= 8 and (len(password)) <= 20:
        factor = True
        if re.search("[a-z]", password):
            factor = True
            if re.search("[A-Z]", password):
                factor = True
                if re.search("[0-9]", password):
                    print('')
                    print('password valid')
                else:
                    print('password does not contain numbers')
            else:
                print("password does not contain uppercase")
        else:
            print('pasword does not contain lowercase letters')
    elif (len(password)) <= 8:
        print('password does not have 8 characters')
    else:
        print('passwrod is more that 20 characters')
    factor = False
