import win32api, win32con
from time import sleep
from userinfo import username, password
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from PIL import ImageGrab
import os
import time

"""

All coordinates assume a screen resolution of 1280x1024, and Chrome 
maximized with the Bookmarks Toolbar enabled.
Down key has been hit 4 times to center play area in browser.
x_pad = 156
y_pad = 345
Play area =  x_pad+1, y_pad+1, 796, 825
"""


# Globals
#-------------------
x_pad = -1
y_pad = 95


class WebkinzBot():

    def __init__(self):
        self.driver = webdriver.Chrome()

        #enabling flash for this browsing session
        self.driver.get("chrome://settings/content/siteDetails?site=https%3A%2F%2Fwww.webkinz.com")

        root1 = self.driver.find_element_by_tag_name('settings-ui')
        shadow_root1 = self.driver.execute_script('return arguments[0].shadowRoot', root1)

        root2 = shadow_root1.find_element_by_tag_name('settings-main')
        shadow_root2 = self.driver.execute_script('return arguments[0].shadowRoot', root2)

        root3 = shadow_root2.find_element_by_tag_name('settings-basic-page')
        shadow_root3 = self.driver.execute_script('return arguments[0].shadowRoot', root3)

        root4 = shadow_root3.find_element_by_tag_name('settings-privacy-page')
        shadow_root4 = self.driver.execute_script('return arguments[0].shadowRoot', root4)

        root5 = shadow_root4.find_element_by_css_selector('#pages > settings-subpage > site-details')
        shadow_root5 = self.driver.execute_script('return arguments[0].shadowRoot', root5)

        root6 = shadow_root5.find_element_by_css_selector('#plugins')
        shadow_root6 = self.driver.execute_script('return arguments[0].shadowRoot', root6)

        permission_select = Select(shadow_root6.find_element_by_css_selector('#permission'))
        permission_select.select_by_value('allow')

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

    def daily_activities(self):
        #screenGrab()
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




bot = WebkinzBot()
bot.login()
bot.daily_activities()
