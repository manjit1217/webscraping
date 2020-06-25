import requests
import pprint
pp = pprint.PrettyPrinter(indent=4)
from selenium import webdriver


class Medium:
    def __init__(self):

res=requests.get('https://medium.com/topic/popular')
print(res.text)