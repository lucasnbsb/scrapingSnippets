# # install chrome
# sudo apt-get -y install google-chrome-stable

# # Download chromedriver
# sudo chmod 0755 /path/to/chromedriver


# Default imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import requests
from bs4 import BeautifulSoup
import time

# visit the page
driver = webdriver.Chrome('/home/lucas/chromedriver')
driver.get("https://www.redbubble.com/people/Paigeonapage/explore?page=1&sortOrder=recent")
driver.maximize_window()
time.sleep(2)

# slow scroll down to the bottom
height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
    time.sleep(0.001)


# Run a regex in a string https://regex101.com/ to test the regex
filename = re.search(r'https.*net/(.*)/.*\.jpg', _string)

