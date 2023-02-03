# first little incursion into scraping. Does not work propperly since the page has a infinite scroll feature that lazy loads more images
# Going into selenium webdriver to fix this next

import re
import requests
from bs4 import BeautifulSoup
site = 'https://www.redbubble.com/people/paigeonapage/shop'
response = requests.get(site)
soup = BeautifulSoup(response.text, 'html.parser')
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