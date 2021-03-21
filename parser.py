from bs4 import BeautifulSoup, SoupStrainer
import requests
from fake_useragent import UserAgent
import os
import time

url = input('Put your url here:   ')
ua = UserAgent()
chr = ua.chrome
req = requests.get(url)
cookie = req.cookies
print(cookie)
get_html = requests.get(url, cookies = cookie, headers = {"User-Agent": chr})
# cookie = ""
# response = requests.get(url)
soup = BeautifulSoup(get_html.content, 'html.parser')
# html_data = soup.prettify
# doc = open("doc.html", 'w')
# doc.write(soup.prettify())
# doc.close()
# parse_only = SoupStrainer('b')
# local_doc = '/home/mirinda/Pycharm/rep_from_dev/doc.html'
# contents = open(local_doc , 'r')
# contents = contents.read()
# soup2 = BeautifulSoup(contents, 'html5lib')

filter_id = soup.find_all('div', class_= 'col dsk-span-12 item-box-hash')
for id in filter_id:
    print(id.text)
    clear_id = id.text

filter_things = soup.find_all('div', class_="col dsk-span-9 tbt-span-8 mob-span-12 spec-data text-left text-bold text-em-5")
for things in filter_things:
    print(things.text)
    clear_things = things.text

filter_price = soup.find_all('b', class_="text-em-5")
for price in filter_price:
    clear_price = price.text.replace('USD', '')
    print(clear_price)


filter_stock = soup.find_all('div', class_="text-status-green col-mt10 text-em-2")
for stock in filter_stock:
    print(stock.text)

filter_not_in_stock = soup.find_all('span', class_="col-mr10 text-mid text-em-5")
for not_stock in filter_not_in_stock:
    print(not_stock.text)

detail_type = soup.find_all('span', {'data-key': 'i27'})
for type in detail_type:
    print(type.text)
    clear_detail_type = type.text

detail_size = soup.find_all('span', {'data-key': 'i0'}, class_="filter-spec no-mob")
for size in detail_size:
    print(size.text)
    clear_detail_size = size.text

detail_hd = soup.find_all('span', {'data-key': 'i2'})
for hd in detail_hd:
    print(hd.text)
    clear_detail_size = hd.text


detail_surface_type = soup.find_all('span', {'data-key': 'i3'})
for surface in detail_surface_type:
    print(surface.text)
    clear_detail_surface_type = surface.text

detail_connector = soup.find_all('span', {'data-key': 'i23'})
for con in detail_connector:
    print(con.text)
    clear_detail_connector = con.text

detail_fix = soup.find_all('span', {'data-key': 'i24'})
for fix in detail_fix:
    print(fix.text)
    clear_detail_fix = fix.text