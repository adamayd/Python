#!/usr/locla/bin/python3

import requests
from bs4 import BeautifulSoup
import random

URL = "https://coronavirus.jhu.edu/map.html"

page = requests.get(URL)

soup = bs4.BeautifulSoup(response.content, "html.parser")

print(page.content)
