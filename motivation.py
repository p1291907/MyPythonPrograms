from bs4 import BeautifulSoup
import pandas as pd
import requests
import urllib.request
import random
def great_quotes():
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text , 'html.parser')
    quoteblocks = soup.find_all('div', class_= 'quote')
#author = soup.find_all('small', class_ = "author")
#if quoteblocks:
    quoteblock = random.choice(quoteblocks)
    quote_text = quoteblock.find('span', class_ = 'text').get_text()
    author = quoteblock.find('small', class_ = 'author').get_text()
    print(f"{quote_text}\n- {author}")
#else:
 # print("NO RESPONSE")
#for i in quoteText:
    #print(i.get_text())
#for i in quoteText:
 #   print(i.text.strip())
answer = input("How are you today? Enter good or bad: ").lower()
if answer == "bad":
    great_quotes()
else:
    print("Great!")
input("Close the terminal to exit")


