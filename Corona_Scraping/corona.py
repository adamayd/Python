#!/usr/locla/bin/python3

import requests
from bs4 import BeautifulSoup
#import random

URL = "https://www.worldometers.info/coronavirus/"

response = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")

rows = soup.find('tbody').find_all('tr')

corona_headers = [
                    "Country",
                    "Total Cases",
                    "New Cases",
                    "Total Deaths",
                    "Total Recovered",
                    "Active Cases",
                    "Serious/Critical",
                    "Top Cases"
                ]

for i in rows:
    print("----> ", i)

