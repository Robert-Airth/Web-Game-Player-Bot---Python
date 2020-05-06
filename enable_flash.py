from selenium.webdriver.support.ui import Select


def enable_flash(driver):

    # enabling flash for this browsing session
    driver.get("chrome://settings/content/siteDetails?site=https%3A%2F%2Fwww.webkinz.com")

    root1 = driver.find_element_by_tag_name('settings-ui')
    shadow_root1 = driver.execute_script('return arguments[0].shadowRoot', root1)

    root2 = shadow_root1.find_element_by_tag_name('settings-main')
    shadow_root2 = driver.execute_script('return arguments[0].shadowRoot', root2)

    root3 = shadow_root2.find_element_by_tag_name('settings-basic-page')
    shadow_root3 = driver.execute_script('return arguments[0].shadowRoot', root3)

    root4 = shadow_root3.find_element_by_tag_name('settings-privacy-page')
    shadow_root4 = driver.execute_script('return arguments[0].shadowRoot', root4)

    root5 = shadow_root4.find_element_by_css_selector('#pages > settings-subpage > site-details')
    shadow_root5 = driver.execute_script('return arguments[0].shadowRoot', root5)

    root6 = shadow_root5.find_element_by_css_selector('#plugins')
    shadow_root6 = driver.execute_script('return arguments[0].shadowRoot', root6)

    permission_select = Select(shadow_root6.find_element_by_css_selector('#permission'))
    permission_select.select_by_value('allow')

    return driver
