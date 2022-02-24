import random
from getpass import getpass

live = int(3)
op_live = int(3)


while True:
    mode = input('would you like play singleplayer or multiplayer: ')
    if mode == 'single' or mode == 'singleplayer':
        print('\nwelcome to singleplayer mode you will be facing against a robot')
        while live > 0 and op_live > 0:
            com_choice1 = ['rock', 'paper', 'scissor']
            com = random.choice(com_choice1)
            print('''
This is a rock,paper,scissor game 
1.rock
2.paper
3.scissor
4.quit \n''')
            choice1 = input('What would be your choice:')
            print()
            if choice1 == '1' or choice1 == 'rock' or choice1 == 'Rock' or choice1 == 'ROCK':
                print('your choice is rock')
                if com == 'rock':
                    print('opponent pick rock')
                    print('DRAW')
                elif com == 'paper':
                    print('oppenent pick paper')
                    print('You lose')
                    live -= 1
                else:
                    print('opponent pick scissor')
                    print('you win')
                    op_live -= 1

            elif choice1 == '2' or choice1 == 'paper' or choice1 == 'Paper' or choice1 == 'PAPER':
                print('your choice is paper')
                if com == 'rock':
                    print('opponent pick rock')
                    print('you win')
                    op_live -= 1

                elif com == 'paper':
                    print('oppenent pick paper')
                    print('DRAW')
                else:
                    print('opponent pick scissor')
                    print('you lose')
                    live -= 1
            elif choice1 == '3' or choice1 == 'scissor' or choice1 == 'Scissor' or choice1 == 'SCISSOR':
                print('your choice is scissor')
                if com == 'rock':
                    print('opponent pick rock')
                    print('you lose')
                    live -= 1
                elif com == 'paper':
                    print('oppenent pick paper')
                    print('You win')
                    op_live -= 1
                else:
                    print('opponent pick scissor')
                    print('DRAW')
            elif choice1 == '4' or choice1 == 'quit' or choice1 == 'Quit' or choice1 == 'QUIT':
                break
            else:
                print('wrong input!')

            print()
            print('your live remaining:', live)
            print('opponent live remaining:', op_live)
            print('______________________________')
            print()
        if live >= 1:
            print('you win')
        else:
            print('you lose')
        break

################################################################################################################
###############################################################################################################

    elif mode == 'multi' or mode == 'multiplayer':
        print('multiplayer mode')
        player1 = input('player1 name: ')
        player2 = input('player2 name: ')
        while live > 0 and op_live > 0:
            com_choice1 = ['rock', 'paper', 'scissor']
            com = random.choice(com_choice1)
            print('''
This is a rock,paper,scissor game 
1.rock
2.paper
3.scissor
4.quit \n''')
            choice1 = getpass('player1 What would be pick: ')
            choice2 = getpass('player2 What would be pick: ')
            print()
            if choice1 == '1' or choice1 == 'rock' or choice1 == 'Rock' or choice1 == 'ROCK':
                print(player1, 'choice is rock')
                if choice2 == '1' or choice2 == 'rock' or choice2 == 'Rock' or choice2 == 'ROCK':
                    print(player2, ' pick rock')
                    print('DRAW')
                elif choice2 == '2' or choice2 == 'paper' or choice2 == 'Paper' or choice2 == 'PAPER':
                    print(player2, 'pick paper')
                    print('You lose')
                    live -= 1
                elif choice2 == '3' or choice2 == 'scissor' or choice2 == 'Scissor' or choice2 == 'SCISSOR':
                    print(player2, ' pick scissor')
                    print('you win')
                    op_live -= 1
                else:
                    print(player2, 'wrong input!')

            elif choice1 == '2' or choice1 == 'paper' or choice1 == 'Paper' or choice1 == 'PAPER':
                print(player1, 'choice is paper')
                if choice2 == '1' or choice2 == 'rock' or choice2 == 'Rock' or choice2 == 'ROCK':
                    print(player2, ' pick rock')
                    print('you win')
                    op_live -= 1
                elif choice2 == '2' or choice2 == 'paper' or choice2 == 'Paper' or choice2 == 'PAPER':
                    print(player2, ' pick paper')
                    print('DRAW')
                elif choice2 == '3' or choice2 == 'scissor' or choice2 == 'Scissor' or choice2 == 'SCISSOR':
                    print(player2, ' pick scissor')
                    print('you lose')
                    live -= 1
                else:
                    print(player2, 'wrong input!')
            elif choice1 == '3' or choice1 == 'scissor' or choice1 == 'Scissor' or choice1 == 'SCISSOR':
                print(player1, ' choice is scissor')
                if choice2 == '1' or choice2 == 'rock' or choice2 == 'Rock' or choice2 == 'ROCK':
                    print(player2, ' pick rock')
                    print('you lose')
                    live -= 1
                elif choice2 == '2' or choice2 == 'paper' or choice2 == 'Paper' or choice2 == 'PAPER':
                    print(player2, ' pick paper')
                    print('You win')
                    op_live -= 1
                elif choice2 == '3' or choice2 == 'scissor' or choice2 == 'Scissor' or choice2 == 'SCISSOR':
                    print(player2, ' pick scissor')
                    print('DRAW')
                else:
                    print(player2, 'wrong input!')
            elif choice1 == '4' or choice1 == 'quit' or choice1 == 'Quit' or choice1 == 'QUIT' or choice2 == '4' or choice2 == 'quit' or choice2 == 'Quit' or choice2 == 'QUIT':
                break
            else:
                print(player1, 'wrong input!')

            print()
            print(player1, 'live remaining:', live)
            print(player2, 'live remaining:', op_live)
            print('______________________________')
            print()
        if live >= 1:
            print(player1, 'win')
        else:
            print(player2, 'win')
        break
    else:
        print()
        print('enter single for SinglePlayer or multi for MultiPlayer')

print('thanks you for playing')
