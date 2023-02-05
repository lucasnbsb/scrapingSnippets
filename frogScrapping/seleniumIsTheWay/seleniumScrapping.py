# # install chrome
# sudo apt-get -y install google-chrome-stable

# # Download chromedriver
# sudo chmod 0755 /path/to/chromedriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import requests
from bs4 import BeautifulSoup
import time



driver = webdriver.Chrome('/home/lucas/chromedriver')
driver.get("https://www.redbubble.com/people/Paigeonapage/explore?page=1&sortOrder=recent")
driver.maximize_window()
time.sleep(2)

# scroll to bottom of page


# slow scroll down to the bottom
height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
    time.sleep(0.001)

page_source = driver.page_source
driver.close()

soup = BeautifulSoup(page_source, 'html.parser')
image_tags = soup.find_all('img')
urls = [img['src'] for img in image_tags]
for url in urls:
    print('\n' + url)
    filename = re.search(r'https.*net/(.*)/.*\.jpg', url)
    if not filename:
         print("Regular expression didn't match with the url: {}".format(url))
         continue
    with open(filename.group(1)+'.jpg', 'wb') as f:
        if 'http' not in url:
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)
print("Download complete, downloaded images can be found in current directory!")



