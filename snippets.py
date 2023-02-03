
# Open the url and read the html into beautiful soup
import requests
from bs4 import BeautifulSoup

url = 'https://www.redbubble.com/people/paigeonapage/shop'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# Run a regex in a string
# https://regex101.com/ to test the regex
import re

filename = re.search(r'https.*net/(.*)/.*\.jpg', _string)
