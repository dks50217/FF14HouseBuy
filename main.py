import os
import sys
import pyautogui
import time
import random
import configparser

config_file_name = 'config.ini'
random.seed(time.time())

# get root 
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)     

# get setting
CONFIG_PATH = os.path.join(application_path, config_file_name)
config = configparser.ConfigParser()
config.read(CONFIG_PATH,encoding="utf-8")

COMMANDS_PERSONAL = config['comm']['personal'].split(',')
COMMANDS_FREECOMPANY= config['comm']['freecompany'].split(',')
GLOBAL_WAIT = float(config['system']['GLOBAL_WAIT'])
RAND_WAIT = float(config['system']['RAND_WAIT'])
START_WAIT = int(config['system']['START_WAIT'])

def try_to_buy(commands):
    # print("\t Waiting")
    time.sleep(RAND_WAIT*random.random() + GLOBAL_WAIT)
    print("\t 開始進行")
    for command in commands:
        try:
            pyautogui.press(command)
            time.sleep(RAND_WAIT*random.random() + GLOBAL_WAIT)
        except KeyboardInterrupt:
            print("結束")
            return False
    return True


def clicking_job(housing_type="freecompany"):
    if housing_type == "freecompany":
        commands = COMMANDS_FREECOMPANY
    else:
        commands = COMMANDS_PERSONAL
    start = time.time()
    print("請立即將畫面切換到FF14，並等待 {0} 秒!".format(START_WAIT))
    time.sleep(START_WAIT)
    count = 1
    loop = True
    while loop:
        print(f"正在嘗試購買, 次數 {count}")
        loop = try_to_buy(commands)
        count += 1
    end = time.time()
    print(f"購買時間: {end-start} 秒!")


clicking_job()
