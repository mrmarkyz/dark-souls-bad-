import random
import time


print('''
▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀     ██████  ▒█████   █    ██  ██▓      ██████    
▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒    ▒██    ▒ ▒██▒  ██▒ ██  ▓██▒▓██▒    ▒██    ▒    
░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░    ░ ▓██▄   ▒██░  ██▒▓██  ▒██░▒██░    ░ ▓██▄      
░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄      ▒   ██▒▒██   ██░▓▓█  ░██░▒██░      ▒   ██▒   
░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄   ▒██████▒▒░ ████▓▒░▒▒█████▓ ░██████▒▒██████▒▒   
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒   ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░   
 ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░   ░ ░▒  ░ ░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░ ▒  ░░ ░▒  ░ ░   
 ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░    ░  ░  ░  ░ ░ ░ ▒   ░░░ ░ ░   ░ ░   ░  ░  ░     
   ░          ░  ░   ░     ░  ░            ░      ░ ░     ░         ░  ░      ░ ''')
input("                             Press Enter to continue...")
game = ['new game', 'continue game', 'settings', 'the game', 'help', 'exit game']
userInput = input('New game\nContinue game\nSettings\nThe game\nHelp\nExit game\nChoose here: ').lower()
if (userInput == 'continue game' or userInput == 'new game'):
    name = input('Name your character: ')
    start = True
while userInput not in game:
    print('That is not an option.\n')
    game = ['new game', 'continue game', 'settings', 'the game', 'help', 'exit game']
    userInput = input('New game\nContinue game\nSettings\nThe game\nHelp\nExit game\nChoose here: ').lower()
    
    if userInput in game:
        start = True
        break


def menu():
    global game
    game = ['new game', 'continue game', 'settings', 'the game', 'help', 'exit game']
    userInput = input('New game\nContinue game\nSettings\nThe game\nHelp\nExit game\nChoose here: ').lower()
    if (game == 'continue game' or game == 'new game'):
        name = input('Name your character: ')
    if userInput not in game:
        print('That is not an option.')


moveCount = 0 
def move():
    move = input('What is your next move? Input MoveList for help: ')
    if (move == 'MoveList'):
        print('''
        Valid moves:
        Forward
        Look around
        Status check
        ''')
    elif (move == 'Forward'):
        global moveCount
        moveCount += 1
        if (moveCount == 5) and not(enemySpawn == 2 or enemySpawn == 8):
            estus = input('Refill your estus? Yes/No: ').lower()
            while(estus == 'yes'):
                if (estusC == 3):
                    print('Wha.. you\'re full!')
                elif (hp <= 200):
                    drink = input('Drink some estus instead? Yes/No: ').lower()
                    if (drink == 'yes'):
                        hp += 150
                elif (estus == 3 and hp > 200):
                    print('You\'re just being greedy now.')
                break
    elif (move == 'Look around'):
        print('''
        The Cemetery of Ash.
        You remember having a long and strenuous battle here.
        Somewhere at least.
        Lots of lightning and dragons.
        You see the fabled Iudex citadel ahead of you.
        What are you doing, daydreaming, Ashen One?
        Persevere.
        Move on.''')

    if (move == 'Status check'):
        print('You have {} hp and {} mana. You have {} estus flasks. Soon enough, you\'ll be able to replenish your estus.' .format(hp, mana, estusC))
    move = input('What is your next move? Input MoveList for help: ')

enemySpawn = random.randint(1,10)    
enemyHP  = random.randint(200, 450)
def spawnEnemy():
    global enemyHP
    global enemySpawn
    enemySpawn = random.randint(1,10)
    enemyHP  = random.randint(200, 450)
    if (enemySpawn == 2 or enemySpawn == 8):
        print('AN ENEMY HAS APPEARED!')
        spawn = True
        if (200 <= enemyHP <= 250):
            print('Wow, what a weakling huh?')
            damage = random.randint(25,50)
            enemyRoll()
        elif (250 < enemyHP <= 350):
            print('The average hollow.')
            damage = random.randint(50,75)
            enemyRoll()
        elif (350 < enemyHP <= 450):
            print('This one is gonna be tough!!')
            damage = random.randint(75,125)
            enemyRoll()

    

def enemyRoll():
    global hp
    if (diff == 'easy'):
        roll = random.randint(1,6)
        if (roll == 2 or roll == 4):
            print('The hollow swings...')
            time.sleep(1)
            print('and...')
            time.sleep(1)
            print('HIT!')
            hit = True
            hp = hp - damage
            print('You have {} hp left.' .format(hp))   
        else:
            print('The hollow missed..')
            hit = False
    elif (diff == 'medium'):
        roll = random.randint(1,6)
        if (roll == 2 or roll == 1 or roll == 3):
            print('The hollow swings...')
            time.sleep(1)
            print('and...')
            time.sleep(1)
            print('HIT!')
            hit = True
            hp = hp - damage
            print('You have {} hp left.' .format(hp))   
        else:
            print('The hollow missed..')
            hit = False
    elif (diff == 'hard'):
        roll = random.randint(1,6)
        if (roll == 1 or roll == 2 or roll == 3 or roll == 4):
            print('The hollow swings...')
            time.sleep(1)
            print('and...')
            time.sleep(1)
            print('HIT!')
            hit = True
            hp = hp - damage
            print('You have {} hp left.' .format(hp))   
        else:
            print('The hollow missed..')
            hit = False
        
def stats():
    print()
    print('Your Soul Level is', SL)
    print('Your vigor is', VIG)
    print('Your attunment is', ATT)
    print('Your endurance is', END)
    print('Your vitality is', VIT)
    print('Your strength is', STR)
    print('Your dexterity is', DEX)
    print('Your intelligence and faith is {} and {}, respectively.' .format(INT, FTH))
    print('Your luck is', LCK)

diff = 'medium'
if (game == 'settings'):
        print('{:>12}\n{:>12}\n{:>12}' .format('Easy', 'Medium', 'Hard'))
        print('{:>12}\n{:>12}\n{:>12}' .format('Enemies have a 1/3 chance of hitting you', 'Enemies have a 1/2 chance of hitting you', 'Enemies have a 2/3 chance of hitting you'))
        diff = input('{:>12}' .format('Choose Difficulty: ').lower())
        menu()
        if (diff != 'easy' or diff != 'medium' or diff != 'hard'):
            print('Choose again, that wasn\'t an option.')
            diff = input('{:>12}' .format('Choose Difficulty: '.lower()))
        else:
            diff == 'medium'


if userInput in game and start == True:
    print('Choose a class.')
    choice = input('''
        Knight
        Mercenary
        Warrior
        Herald
        Thief
        Assassin
        Sorcerer
        Pyromancer
        Deprived
        Choose your class... (CASE SPECIFIC!!)
        Enter selection: ''') 
    if (choice == 'Knight'):
        SL = 9
        VIG = 12
        ATT = 10
        END = 11
        VIT = 15
        STR = 13
        DEX = 12
        INT = 9
        FTH = 9
        LCK = 7
        weapon = 'Longsword'
        shield = 'Knight Shield'
        stats()
    elif (choice == 'Mercenary'):
        SL = 8
        VIG = 11
        ATT = 12
        END = 11
        VIT = 10
        STR = 10
        DEX = 16
        INT = 10
        FTH = 8
        LCK = 9
        weapon = 'Sellsword Twinblades'
        shield = 'Wooden Shield'
        stats()
    elif (choice == 'Warrior'):
        SL = 7
        VIG = 14
        ATT = 6
        END = 12
        VIT = 11
        STR = 16
        DEX = 9
        INT = 8
        FTH = 9 
        LCK = 11
        weapon = 'Battle Axe'
        shield = 'Round Shield'
        stats()
    elif (choice == 'Herald'):
        SL = 9
        VIG = 14
        ATT = 10
        END = 9
        VIT = 12
        STR = 12
        DEX = 11
        INT = 8
        FTH = 13
        LCK = 11
        weapon = 'Spear'
        shield = 'Kite Shield'
        stats()
    elif (choice == 'Thief'):
        SL = 5
        VIG = 10
        ATT = 11
        END = 10
        VIT = 9
        STR = 9
        DEX = 13
        INT = 10
        FTH = 8
        LCK = 14
        weapon = 'Bandit\'s Knife'
        shield = 'Iron Round Shield'
        stats()
    elif (choice == 'Assassin'):
        SL = 10
        VIG = 10
        ATT = 14
        END = 11
        VIT = 10
        STR = 10
        DEX = 14
        INT = 11
        FTH = 9
        LCK = 10
        weapon = 'Estoc'
        shield = 'Target Shield'
        stats()
    elif (choice == 'Sorcerer'):
        SL = 6
        VIG = 9
        ATT = 16
        END = 9
        VIT = 7 
        STR = 7
        DEX = 12
        INT = 16
        FTH = 7
        LCK = 12
        weapon = 'Mail Breaker'
        shield = 'Leather Shield'
        stats()
    elif (choice == 'Pyromancer'):
        SL = 8
        VIG = 11
        ATT = 12
        END = 10
        VIT = 8
        STR = 12
        DEX = 9
        INT = 14
        FTH = 14
        LCK = 7
        weapon = 'Hand Axe'
        shield = 'Caduceus Round Shield'
        stats()
    elif (choice == 'Cleric'):
        SL = 7
        VIG = 10
        ATT = 14
        END = 9
        VIT = 7
        STR = 12
        DEX = 8
        INT = 7
        FTH = 16
        LCK = 13
        weapon = 'Mace'
        shield = 'Blue Wooden Shield'
        stats()
    elif (choice == 'Deprived'):
        SL = 1
        VIG = 10
        ATT = 10
        END = 10
        VIT = 10
        STR = 10
        DEX = 10
        INT = 10
        FTH = 10
        LCK = 10
        weapon = 'Club'
        shield = 'Plank Shield'
        stats()



time.sleep(5)
print(''' 
█     █░▓█████  ██▓     ▄████▄   ▒█████   ███▄ ▄███▓▓█████ 
▓█░ █ ░█░▓█   ▀ ▓██▒    ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀ 
▒█░ █ ░█ ▒███   ▒██░    ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒███   
░█░ █ ░█ ▒▓█  ▄ ▒██░    ▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒▓█  ▄ 
░░██▒██▓ ░▒████▒░██████▒▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░▒████▒
░ ▓░▒ ▒  ░░ ▒░ ░░ ▒░▓  ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░
  ▒ ░ ░   ░ ░  ░░ ░ ▒  ░  ░  ▒     ░ ▒ ▒░ ░  ░      ░ ░ ░  ░
  ░   ░     ░     ░ ░   ░        ░ ░ ░ ▒  ░      ░      ░   
    ░       ░  ░    ░  ░░ ░          ░ ░         ░      ░  ░
                        ░                                   ''')
time.sleep(5)
print('''
▄▄▄█████▓ ▒█████     ▄▄▄█████▓ ██░ ██ ▓█████ 
▓  ██▒ ▓▒▒██▒  ██▒   ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀ 
▒ ▓██░ ▒░▒██░  ██▒   ▒ ▓██░ ▒░▒██▀▀██░▒███   
░ ▓██▓ ░ ▒██   ██░   ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄ 
  ▒██▒ ░ ░ ████▓▒░     ▒██▒ ░ ░▓█▒░██▓░▒████▒
  ▒ ░░   ░ ▒░▒░▒░      ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░
    ░      ░ ▒ ▒░        ░     ▒ ░▒░ ░ ░ ░  ░
  ░      ░ ░ ░ ▒       ░       ░  ░░ ░   ░   
             ░ ░               ░  ░  ░   ░  ░''')
time.sleep(5)
print('''
 ▄████████    ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████     ███        ▄████████    ▄████████ ▄██   ▄         ▄██████▄     ▄████████         ▄████████    ▄████████    ▄█    █▄    
███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ▀█████████▄   ███    ███   ███    ███ ███   ██▄      ███    ███   ███    ███        ███    ███   ███    ███   ███    ███   
███    █▀    ███    █▀  ███   ███   ███   ███    █▀     ▀███▀▀██   ███    █▀    ███    ███ ███▄▄▄███      ███    ███   ███    █▀         ███    ███   ███    █▀    ███    ███   
███         ▄███▄▄▄     ███   ███   ███  ▄███▄▄▄         ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███      ███    ███  ▄███▄▄▄            ███    ███   ███         ▄███▄▄▄▄███▄▄ 
███        ▀▀███▀▀▀     ███   ███   ███ ▀▀███▀▀▀         ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ▄██   ███      ███    ███ ▀▀███▀▀▀          ▀███████████ ▀███████████ ▀▀███▀▀▀▀███▀  
███    █▄    ███    █▄  ███   ███   ███   ███    █▄      ███       ███    █▄  ▀███████████ ███   ███      ███    ███   ███               ███    ███          ███   ███    ███   
███    ███   ███    ███ ███   ███   ███   ███    ███     ███       ███    ███   ███    ███ ███   ███      ███    ███   ███               ███    ███    ▄█    ███   ███    ███   
████████▀    ██████████  ▀█   ███   █▀    ██████████    ▄████▀     ██████████   ███    ███  ▀█████▀        ▀██████▀    ███               ███    █▀   ▄████████▀    ███    █▀    
                                                                                ███    ███                                                                                      ''')
def gamePlay():     
    move()
    spawnEnemy()

                  
hp = VIG * 25
mana = ATT * 10
stam = END * 5
atk = STR * 7.5
randomifier = random.randint(0,2)
pDMG = atk * randomifier

estusC = 3

time.sleep(2)
print('You awaken from your grave, or was it really?')
time.sleep(1.5)
print('Nevermind.')
time.sleep(1)
print('You start with a {} and a {}. You have 3 estus flasks. You use these to heal.'.format(weapon, shield))
time.sleep(1.5)
print('You have {} health.' .format(hp))
time.sleep(1)
print('Your mana count is at {}.' .format(mana))
if (mana < 100):
    time.sleep(3)
    print('Wow..')
    time.sleep(2)
    print('A real brute, huh?')
elif (100 <= mana <= 150):
    print('The average mana count.')
else:
    print('Incredible! You truly are a mastered sorcerer!')
if (stam < 40):
    print('I guess you\'re more meant for the brains, huh?')
elif (40 <= stam <= 50):
    print('The average runner. Good for you!')
elif (stam > 50):
    print('Incredible! You have unmatched stamina!')

ready = input('Are you ready!? Y/N: ').lower()
readyList = ['yes', 'y', 'no', 'n']
if ready == 'yes' or ready == 'y':
    readyCheck = True
while ready not in readyList:
    print('That is not a valid option..')
    ready = input('Are you ready!? Y/N: ').lower()
spawn = False


while start == True and readyCheck == True:
    if hp <= 0:
        print('You swing and stagger..')
        time.sleep(1)
        print('In a daze, your eyes slowly close.')
        time.sleep(2)
        print('''
▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓ 
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░ 
 ░ ░         ░ ░     ░           ░     ░     ░  ░   ░    
 ░ ░                           ░                  ░  ''')
        quit()
    while(ready == 'yes' or ready == 'y' and spawn == False):
        gamePlay()
        if (spawn == True):
            break
    while(spawn == True):
        spawnEnemy()
        moveF = input('What is your next move? You have four moves! Type Movelist for help: ').lower()
        if (moveF == 'movelist'):
            print('Fight\nRoll\nStatus check\nUse Estus')
            moveF = input('What is your next move? You have four moves! Type Movelist for help: ').lower()
        if (moveF == 'fight'):
            print('You take a swing at the hollow..')
            time.sleep(1)
            print('You sucessfully hit the hollow!')
            print('You hit the hollow for', pDMG,'and ')
            enemyRoll()