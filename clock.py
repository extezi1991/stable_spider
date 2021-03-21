import requests, requests.utils, pickle
from bs4 import BeautifulSoup
import requests, json


from fake_useragent import UserAgent
ua = UserAgent()
chr = ua.opera
url = "https://www.laptopscreen.com/English/brand/Gateway/"



def get_cookies():
    req = requests.get(url)
    cookie = req.cookies
    ses = cookie.values()
    cook = (','.join(ses))
    cookie_file = open('/home/mirinda/Pycharm/rep_from_dev/cookie.txt', "w")
    cookie_file.write(str(cook))
    cookie_file.close()

get_cookies()

