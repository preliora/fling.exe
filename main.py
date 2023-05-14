import keyboard
from time import sleep
import os

settings = {"seconds": 0.075, "times": 10, "hotkey": "f"}
os.system('title FLING.EXE')

print("""  \033[35m______ _      _____ _   _  _____   ________   ________ 
 |  ____| |    |_   _| \ | |/ ____| |  ____\ \ / /  ____|
 | |__  | |      | | |  \| | |  __  | |__   \ V /| |__   
 |  __| | |      | | | . ` | | |_ | |  __|   > < |  __|  
 | |    | |____ _| |_| |\  | |__| |_| |____ / . \| |____ 
 |_|    |______|_____|_| \_|\_____(_)______/_/ \_\______|
                                                         
                                                         """)

def punch():
    for i in range(settings['times']):
        keyboard.press('w')
        sleep(settings['seconds'])
        keyboard.release('w')
        keyboard.press('a')
        sleep(settings['seconds'])
        keyboard.release('a')
        keyboard.press('s')
        sleep(settings['seconds'])
        keyboard.release('s')
        keyboard.press('d')
        sleep(settings['seconds'])
        keyboard.release('d')
    print('\033[31mrip \033[32m:(')

def command(c):
    
    if c.find('speed') != -1:
        settings['seconds'] = float(c.split('speed')[1])
    elif c.find('times') != -1:
        settings['times'] = int(c.split('times')[1])
    elif c.find('hotkey') != -1:
        settings['hotkey'] = c.split('hotkey')[1].split(' ')[1]
        print(settings['hotkey'])
    else:
        print(c + " \033[37mis not a command")
        print("\033[35m=============================================")

while True:
    if keyboard.read_key() == settings['hotkey']:
        punch()
    if keyboard.read_key() == "c":
        cmd = input("cmd:")
        command(cmd)
    if keyboard.read_key() == "`":
        os.system('cls')
        print("""  \033[35m______ _      _____ _   _  _____   ________   ________ 
 |  ____| |    |_   _| \ | |/ ____| |  ____\ \ / /  ____|
 | |__  | |      | | |  \| | |  __  | |__   \ V /| |__   
 |  __| | |      | | | . ` | | |_ | |  __|   > < |  __|  
 | |    | |____ _| |_| |\  | |__| |_| |____ / . \| |____ 
 |_|    |______|_____|_| \_|\_____(_)______/_/ \_\______|
                                                         
                                                         """)

