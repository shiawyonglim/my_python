import re
from getpass import getpass

print('password msut contain 8-20 Letters( Uppercase , Lowercase )and Number')
password = getpass('enter your password:')
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
                    print('password valid')
                    while True:
                        show = input(
                            'Do you want to see your password yes or no: ')
                        if show == 'yes' or show == 'Yes' or show == 'YES':
                            print(password)
                            break
                        elif show == 'no' or show == 'No' or show == 'NO':
                            break
                        else:
                            print()
                            print('please enter yes or no')
                else:
                    print('password does not contain numbers')
            else:
                print("password does not contain uppercase")
        else:
            print('pasword does not contain lowercase')
    elif (len(password)) <= 8:
        print('password does not have 8 characters')
    else:
        print('passwrod is more that 20 characters')
    break
