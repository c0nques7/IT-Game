import time
import random
import cmd
import textwrap
import sys
import os
import time

screen_width = 100

##### Player Setup #####
class player:
        def __int__(self):
            self.name = 0
            self.mh = 0
            self.location = "start"
            self.gameover = False
myPlayer = player()

##### Title Screen #####
def title_screen_selections():
        option = input("> ")
        if option.lower() == ("play"):
            start_game() #placeholder
        elif option.lower("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()
        while option.lower() not in ['play', 'help', 'quit']:
            print("Please enter a vaild command.")
        option = input("> ")

def title_screen():
    os.system('clear')
    print('############################')
    print('#  Welcom to the IT Game!  #')
    print('############################')
    print('         - Play -           ')
    print('         - Help -           ')
    print('         - Quit -           ')
    print(' Copyright 18 Conquest Games')
    title_screen_selections()

def help_menu():
    print('############################')
    print('#  Welcom to the IT Game!  #')
    print('############################')
    print('- Use the command "queue" to check items in your queue -')
    print('- Check your health to make sure you survive the job -')
    print('- Make sure your boss doesnt catch you working on certs! -')
    print('- Have fun! -')
    title_screen_selections()



##### Locations #####
#Your Office
#Copy Room
#C Level Suite
#Manager's Office
#Break Room
#HR
#The Cube Pit

DESCRIPTION = 'description'
TICKET = 'ticket'
CHECK_QUEUE = 'queue'
COMPLETED = False
YOUR_OFFICE = 'office'
COPY_ROOM = 'copy'
C_LEVEL = 'coffice'
MANAGER_OFFICE = 'moffice'
BREAK_ROOM = 'break'
HR = 'hr'
CUBE_PIT = 'cube'

solved_tickets = {'copy': False, 'coffice': False, 'moffice': False, 'break': False, 'hr': False, 'cube': False }

zonemap = {
    'copy':{
        ZONENAME:"",
        DESCRIPTION: 'description',
        TICKET: 'ticket',
        CHECK_QUEUE: 'queue',
        COMPLETED: False,
    },
    'coffice':{
        ZONENAME:"",
        DESCRIPTION: 'description',
        TICKET: 'ticket',
        CHECK_QUEUE: 'queue',
        COMPLETED: False,
    },
    'moffice':{
        ZONENAME:"",
        DESCRIPTION: 'description',
        TICKET: 'ticket',
        CHECK_QUEUE: 'queue',
        COMPLETED: False,
    },
    'break':{
        ZONENAME:"",
        DESCRIPTION: 'description',
        TICKET: 'ticket',
        CHECK_QUEUE: 'queue',
        COMPLETED: False,
    },
    'hr':{
        ZONENAME:"",
        DESCRIPTION: 'description',
        TICKET: 'ticket',
        CHECK_QUEUE: 'queue',
        COMPLETED: False,
    },
    'cube':{
        ZONENAME:"",
        DESCRIPTION: 'description',
        TICKET: 'ticket',
        CHECK_QUEUE: 'queue',
        COMPLETED: False,
    },
    'office':{
        ZONENAME:'home',
        DESCRIPTION: 'description',
        TICKET: 'ticket',
        CHECK_QUEUE: 'queue',
        COMPLETED: False,
    },


}

##### Game Interactivity #####
def print_location():
    print('\n' + myPlayer.location)
    print(zonemap[myPlayer.location][DESCRIPTION])

def prompt():
    print('\n' + "_______________________")
    print("what would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'work', 'fix', 'code', 'study', 'queue']
    while action.lower() not in acceptable_actions:
        print("Yeah, that's not gonna work. Try something else. \n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['work', 'fix', 'code', 'study', 'queue']:
        player_examine(action.lower())

def player_move(myAction):
    ask = "where would you like to move to?\n"
    dest = input(ask)
    if dest == in ['copy']:
        destination = zonemap.[myPlayer.location][COPY_ROOM]
        movement.handler(destination)
    elif dest == in ['office']:
        destination = zonemap.[myPlayer.location][YOUR_OFFICE]
        movement.handler(destination)
    elif dest == in ['coffice']:
        destination = zonemap.[myPlayer.location][C_LEVEL]
        movement.handler(destination)
    elif dest == in ['moffice']:
        destination = zonemap.[myPlayer.location][MANAGER_OFFICE]
        movement.handler(destination)
    elif dest == in ['break']:
        destination = zonemap.[myPlayer.location][BREAK_ROOM]
        movement.handler(destination)
    elif dest == in ['hr']:
        destination = zonemap.[myPlayer.location][HR]
        movement.handler(destination)
    elif dest == in ['cube']:
        destination = zonemap.[myPlayer.location][CUBE_PIT]
        movement.handler(destination)

def movement_handler(destination):
    print("\n" + "You're now in the " + destination +".")
    myPlayer.location = destination
    print_location()

def player_examine[action]:
    if zonemap[]myPlayer.location[SOLVED]:
        print("All the tickets are complete here.")
    else
        print["You can trigger puzzles here."]






##### Game Functionality #####
def start_game():
    return

def main_game_loop():
    while myPlayer.gameover is False:
    prompt()
    #here is where we need to decide end game, levels, etc

def setup_game():
    os.system('clear')
    question1 = "Whats your name?\n"
    for character in question1:
        sys.stdout.write(character):
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

### Introduction ###

question3 = "Welcome to the company, " + player_name
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    os.system('clear')
    print("#################")
    print("Lets get to work!")
    print("#################")
    main_game_loop()






title_screen()