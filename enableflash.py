from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
prefs = {
    "profile.default_content_setting_values.plugins": 1,
    "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
    "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
    "PluginsAllowedForUrls": "http://webkinz.com"
}

options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(options=options)