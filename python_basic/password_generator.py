import random
import array

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

rnd_num = random.choice(number)
rnd_low = random.choice(lower)
rnd_up = random.choice(upper)
rnd_all = number+lower+upper

rnd = rnd_low+rnd_num+rnd_up

print('password must be more that 4 letters')

while True:
    passLen = int(input('how long would you like the password lenght to be: '))
    if passLen >= 4:
        for x in range(passLen - 3):
            rnd = rnd + random.choice(rnd_all)
            temp_pass_list = array.array('u', rnd)
            random.shuffle(temp_pass_list)
        password = ""
        for x in temp_pass_list:
            password = password + x
        print(password)
        break
    else:
        print('\nplease enter 4 or more letters')
