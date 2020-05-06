import win32api, win32con
from time import sleep
from userinfo import username, password
from enable_flash import enable_flash
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from PIL import ImageGrab
import os
import time

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

        self.driver = webdriver.Chrome()
        self.driver = enable_flash(self.driver)

    def screenGrab(self):
        box = (x_pad+1, y_pad+1, x_pad + 1344, y_pad + 972)
        im = ImageGrab.grab(box)
        im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
                '.png', 'PNG')

    def leftClick(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(.1)
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
        self.driver.get('http://webkinz.com')
        #goes to home page and clicks "play" button
        login_button = self.driver.find_element_by_id('btn-play-img')
        login_button.click()

        #saving base window
        base_window = self.driver.window_handles[0]
        #switching windows
        self.driver.switch_to.window(self.driver.window_handles[1])

        # enters username and password and submits
        username_field = self.driver.find_element_by_id('login_name')
        password_field = self.driver.find_element_by_id('user_password')
        login_button = self.driver.find_element_by_id('login')
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        sleep(15)
        self.driver.maximize_window()

    def close_landing_alerts(self):
        #if screen_shade != normal_screen_shade{code below}:
        #click daily delivery popup
        self.mousePos((782, 277))
        self.leftClick()
        time.sleep(1.5)
        #}

    def daily_activities(self):
        #screenGrab()

        #closes daily delivery alert
        self.close_landing_alerts()

        #click menu button
        self.mousePos((1290, 932))
        self.leftClick()
        time.sleep(1.5)

        #click today's activities
        self.mousePos((841, 129))
        self.leftClick()
        time.sleep(2.5)

        #scroll to bottom of today's activities
        self.mousePos((710, 567))
        for i in range(25):
            self.leftClick()
        time.sleep(0.1)

        #select bottom-most desired activity
        self.mousePos((681, 561))
        self.leftClick()
        time.sleep(5)

        #click "spin" on wheel of wishes
        self.mousePos((733, 616))
        self.leftClick()
        time.sleep(5)
        self.leftClick()
        time.sleep(5)

        #click on "ok" for congrats alert after winning or not
        self.mousePos((722, 414))
        self.leftClick()
        time.sleep(5)

        # click menu button
        self.mousePos((1290, 932))
        self.leftClick()
        time.sleep(1.5)

        #click today's activities
        self.mousePos((841, 129))
        self.leftClick()
        time.sleep(2.5)

        #scroll to bottom of today's activities
        self.mousePos((710, 567))
        for i in range(25):
            self.leftClick()
        time.sleep(0.1)

        #select bottom - 1 desired activity
        self.mousePos((681, 503))
        self.leftClick()
        time.sleep(5)

        # click "spin" on wheel of deluxe
        self.mousePos((676, 599))
        self.leftClick()
        time.sleep(5)
        self.leftClick()
        time.sleep(5)

        # click on "ok" for congrats alert after winning or not
        self.mousePos((722, 414))
        self.leftClick()
        time.sleep(5)

        # click menu button
        self.mousePos((1290, 932))
        self.leftClick()
        time.sleep(1.5)

        # click today's activities
        self.mousePos((841, 129))
        self.leftClick()
        time.sleep(2.5)

        # scroll to bottom of today's activities
        self.mousePos((710, 567))
        for i in range(25):
            self.leftClick()
        time.sleep(0.1)

        # select bottom - 2 desired activity
        self.mousePos((681, 324))
        self.leftClick()
        time.sleep(5)

        # # click "spin" on wheel of wow
        # self.mousePos((733, 616))
        # self.leftClick()
        # time.sleep(5)
        # self.leftClick()
        # time.sleep(5)

        # # click on "ok" for congrats alert after winning or not
        # self.mousePos((722, 414))
        # self.leftClick()
        # time.sleep(5)
        #
        # # click menu button
        # self.mousePos((1290, 932))
        # self.leftClick()
        # time.sleep(1.5)
        #
        # # click today's activities
        # self.mousePos((841, 129))
        # self.leftClick()
        # time.sleep(2.5)
        #
        # # scroll to bottom of today's activities
        # self.mousePos((710, 567))
        # for i in range(25):
        #     self.leftClick()
        # time.sleep(0.1)
        #
        # # select bottom - 3 desired activity
        # self.mousePos((681, 293))
        # self.leftClick()
        # time.sleep(5)





bot = WebkinzBot()
bot.login()
#bvvvvvvvvvvvvvvv`v     v   v bot.daily_activities()
