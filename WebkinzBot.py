import win32api
import win32con
from time import sleep
from userinfo import userlist1, userlist2
from enable_flash import enable_flash
from selenium import webdriver
from PIL import ImageGrab, ImageOps
from numpy import *
from pynput import keyboard
from pynput.keyboard import Key, Listener
import os
import time
import sys
import threading

"""

All coordinates assume a screen resolution of 1920 x 1080, and Chrome 
maximized with the Bookmarks Toolbar disabled.
x_pad = -1
y_pad = 95
Play area =  x_pad+1, y_pad+1, 1344, 972
"""


# Globals
#-------------------
x_pad = -1
y_pad = 95


class WebkinzBot():

    def __init__(self):
        self.account = input("Which account would you like to log into? Type ''rob'', ''hayley'', or ''paulette'') ")
        self.driver = webdriver.Chrome()
        self.driver = enable_flash(self.driver)

    def __init__(self, userchoice):
        self.account = userchoice
        self.driver = webdriver.Chrome()
        self.driver = enable_flash(self.driver)



    def screenGrab(self):
        box = (x_pad+1, y_pad+1, x_pad + 1344, y_pad + 972)
        im = ImageGrab.grab(box)
        im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
                '.png', 'PNG')
        sleep(0.01)

    def leftClick(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def leftDown(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(1)

    def leftUp(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(.1)

    def mousePos(self, cord):
        win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

    def get_coords(self):
        x, y = win32api.GetCursorPos()
        x = x - x_pad
        y = y - y_pad

    def login(self):
        username = userlist1[self.account][0]
        password = userlist1[self.account][1]
        self.driver.get('http://webkinz.com')
        # goes to home page and clicks "play" button
        login_button = self.driver.find_element_by_id('btn-play-img')
        login_button.click()

        # saving base window
        base_window = self.driver.window_handles[0]
        # switching windows
        self.driver.switch_to.window(self.driver.window_handles[1])


        # enters username and password and submits
        username_field = self.driver.find_element_by_id('login_name')
        password_field = self.driver.find_element_by_id('user_password')
        login_button = self.driver.find_element_by_id('login')
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        self.driver.maximize_window()
        sleep(25)

        # close landing alerts
        self.close_landing_alerts()


    def quit(self):
        self.driver.quit()

    def close_landing_alerts(self):
        #if screen_shade != normal_screen_shade{code below}:
        #click daily delivery popup
        self.mousePos((782, 277))
        self.leftClick()
        time.sleep(.3)

        self.mousePos((991, 331))
        self.leftClick()
        time.sleep(.3)

    def click_game_button(self):
        # click game button
        self.mousePos((1209, 888))
        self.leftClick()
        time.sleep(6)

    def click_menu_button(self):
        # click menu button
        self.mousePos((1290, 932))
        self.leftClick()
        time.sleep(2)

    def click_wish_factory(self):
        # click game button
        self.mousePos((842, 780))
        self.leftClick()
        time.sleep(2)

    def click_vacation_island(self):
        # click game button
        self.mousePos((842, 562))
        self.leftClick()
        time.sleep(2)


    def click_wheel_of_wow(self):
        #click wheel of wow
        self.mousePos((486, 289))
        self.leftClick()
        time.sleep(1)
        self.mousePos((853, 542))
        self.leftClick()
        time.sleep(2.5)

    def click_wheel_of_deluxe(self):
        # click wheel of deluxe
        self.mousePos((485, 352))
        self.leftClick()
        time.sleep(.3)
        self.mousePos((853, 542))
        self.leftClick()
        time.sleep(2.5)

    def click_wish_factory(self):
        # click wish factory
        self.mousePos((842, 780))
        self.leftClick()
        time.sleep(8)

    def click_wheel_of_wishes(self):
        # click wish factory
        self.mousePos((410, 667))
        self.leftClick()
        time.sleep(6)

    def click_vacation_island(self):
        # click vacation island
        self.mousePos((842, 562))
        self.leftClick()
        time.sleep(3)

    def click_vacation_wheel(self):
        # click vacation wheel
        self.mousePos((891, 215))
        self.leftClick()
        time.sleep(5)

    def scroll_games(self, num):
        self.mousePos((494, 533))
        for i in range(0, num):
            self.leftClick()
            time.sleep(.1)

    def open_wacky_zingos_extreme(self):
        # open game menu
        self.click_game_button()

        # scroll down menu 5 times
        self.scroll_games(5)

        # click wacky zingos
        self.mousePos((486, 486))
        self.leftClick()
        time.sleep(1)
        self.mousePos((853, 542))
        self.leftClick()
        time.sleep(2)

    def play_wheel_of_wow(self):
        # click wheel of wow
        self.click_wheel_of_wow()

        # click "spin" on wheel of wow
        self.mousePos((676, 599))
        self.leftClick()
        time.sleep(5)
        self.leftClick()
        time.sleep(3)

        # click on no-spins alert
        self.mousePos((775, 482))
        self.leftClick()

        # click on "ok" for congrats alert after winning or not
        self.mousePos((722, 414))
        self.leftClick()
        time.sleep(5)


    def play_wheel_of_deluxe(self):
        # click wheel of wow
        self.click_wheel_of_deluxe()

        # click "spin" on wheel of wow
        self.mousePos((676, 599))
        self.leftClick()
        time.sleep(3)
        self.leftClick()
        time.sleep(3)


        # click on "ok" for congrats alert after winning or not
        self.mousePos((722, 414))
        self.leftClick()
        time.sleep(5)

    def play_wheel_of_wishes(self):
        # click menu button
        self.click_menu_button()

        # click wish factory
        self.click_wish_factory()

        # click wheel of wishes
        self.click_wheel_of_wishes()

        # click "spin" on wheel of wishes
        self.mousePos((733, 616))
        self.leftClick()
        time.sleep(5)
        self.leftClick()
        time.sleep(5)

        # click on "ok" for congrats alert after winning or not
        self.mousePos((722, 414))
        self.leftClick()
        time.sleep(5)

    def play_vacation_wheel(self):
        # click menu button
        self.click_menu_button()

        # click vacation island
        self.click_vacation_island()

        # click vacation wheel
        self.click_vacation_wheel()

        # click "spin" on vacation wheel
        self.mousePos((675, 600))
        self.leftClick()
        time.sleep(6)
        self.leftClick()
        time.sleep(6)

        # click on "ok" for congrats alert after winning or not
        self.mousePos((722, 414))
        self.leftClick()
        time.sleep(5)




    def daily_activities(self):


        # closes daily delivery alert
        self.close_landing_alerts()

        # click game button
        self.click_game_button()

        # play wheel of wow
        self.play_wheel_of_wow()

        # click game button
        self.click_game_button()

        # play wheel of deluxe
        self.play_wheel_of_deluxe()

        # play wheel of wishes
        self.play_wheel_of_wishes()

        # play vacation wheel
        self.play_vacation_wheel()




    def play_wacky_zingos_extreme(self):

        # click play button
        self.mousePos((740, 642))
        self.leftClick()
        time.sleep(.3)

        # select hyperclub and double hit options
        self.mousePos((665, 398))
        self.leftClick()
        time.sleep(.3)

        # play 5 tries of game

        for i in range(0, 5):
            clickmore = True

            time.sleep(.5)


            self.wacky_zingo_extreme_swing()

            # if the screen is not the ready screen, try clicking alert to reset
            # to the ready screen for the next round
            j = 0
            if i == 4:
                end_state = ImageOps.grayscale(self.screen_grab(286, 158, 364, 213))
                end_state = array(end_state.getcolors())
                end_state = end_state.sum()
                print(end_state)
            while clickmore is True:
                if j < 100:
                    self.mousePos(((600 + mod(j, 100)), int(floor(500 + (mod(j, 100) * 0.5)))))
                    self.leftClick()

                if j < 200 and j >= 100:
                    self.mousePos(((650 + mod(j, 100)), int(floor(500 + (mod(j, 100) * 0.5)))))
                    self.leftClick()

                if j < 300 and j >= 200:
                    self.mousePos(((700 + mod(j, 100)), int(floor(500 + (mod(j, 100) * 0.5)))))
                    self.leftClick()
                if j == 290:
                    time.sleep(20)

                time.sleep(.1)

                j = mod((j + 10), 300)

                if (i < 4):
                    current_state = ImageOps.grayscale(self.screen_grab(859, 178, 946, 293))
                    current_state = array(current_state.getcolors())
                    current_state = current_state.sum()
                    print(current_state)
                    if 29000 < current_state and current_state < 33000:
                        clickmore = False

                if (i == 4):
                    current_state = ImageOps.grayscale(self.screen_grab(286, 158, 364, 213))
                    current_state = array(current_state.getcolors())
                    current_state = current_state.sum()
                    print(current_state)
                    if current_state != end_state:
                        clickmore = False



        self.mousePos((560, 544))
        self.leftClick()
        time.sleep(.5)


    def wacky_zingo_extreme_swing(self):
        # first two clicks with delay to initiate swing 1
        self.mousePos((665, 398))
        self.leftClick()
        time.sleep(.48)
        self.leftClick()
        time.sleep(3.1)
        # third click to initiate swing 2
        self.leftClick()
        time.sleep(5)


    def screen_grab(self, x1, y1, x2, y2):
        box = (x1, y1, x2, y2)
        im = ImageGrab.grab(box)
        sleep(0.01)

        return im

# def on_press(key):
#     if key == Key.esc:
#         print("It's dead!")
#         sleep(0.01)
#         os._exit(1)
#         return False
#
#     #     # # Stop listener
#     #     # return False
#     else:
#         print("It's alive!")
#         sleep(0.01)
#         return True

#
# import os
#

# def on_release(key):
#     if key == Key.esc:
#         print("It's dead!")
#         sleep(0.01)
#         os._exit(1)
#         # sys.exit()
#         # Stop listener
#     #     return False
#     else:
#         print("It's alive!")
#         sleep(0.01)
#         return True
#
def play_webkinz():
    bot = WebkinzBot("rob")
    bot.login()
    # bot.daily_activities()
    for i in range(0, 5):
        bot.open_wacky_zingos_extreme()
        bot.play_wacky_zingos_extreme()

def on_press(key):
    if key == Key.esc:
        print("It's dead!")
        sleep(0.01)
        os._exit(1)
        return False

    #     # # Stop listener
    #     # return False
    else:
        print("It's alive!")
        sleep(0.01)
        return True

def main():
    thread2 = threading.Thread(target=play_webkinz, args=())
    thread2.start()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

main()



# bot.daily_activities()
# for i in range(0, 1):
#     bot.open_wacky_zingos_extreme()
#     bot.play_wacky_zingos_extreme()
#




# for user in userlist1:
#     bot = WebkinzBot(userchoice=user)
#     bot.login()
#     bot.daily_activities()
#     for i in range(0, 1):
#         bot.open_wacky_zingos_extreme()
#         bot.play_wacky_zingos_extreme()
#     bot.quit()


# for user in userlist2:
#     bot = WebkinzBot(userchoice=user)
#     bot.login()
# bot.quit()

# bot = WebkinzBot("rob")
# bot.login()
#     #bot.daily_activities()
#     for i in range(0, 1):
#         bot.open_wacky_zingos_extreme()
#         bot.play_wacky_zingos_extreme()
#     bot.quit()
# bot.click_menu_button()

# bot = WebkinzBot("hayley")
# bot.login()
# # bot.daily_activities()
# for i in range(0, 10):
#     bot.open_wacky_zingos_extreme()
#     bot.play_wacky_zingos_extreme()
# bot.daily_activities()
# for i in range(0, 10):
#     bot.open_wacky_zingos_extreme()
#     bot.play_wacky_zingos_extreme()
# bot.quit()

