from bs4 import BeautifulSoup, SoupStrainer
import requests
from fake_useragent import UserAgent
ua = UserAgent()
chr = ua.opera
d = []
from xlsxwriter import *
import pandas as pd

with open('other.txt', 'r') as f:
    for line in f:
        url = str(line.strip('\n'))
        print('Started WEB-Spider....')
        print('---------------------------' + url)

        req = requests.get(str(line))
        cookie = req.cookies
        print(cookie)
        print(line)
        get_html = requests.get(url, cookies=cookie, headers={"User-Agent": chr})
        print(get_html)
        soup = BeautifulSoup(get_html.content, 'html5lib')
        doc_link = open('data.html', 'w')
        file = open('example.csv', 'a')


        doc_link.write(soup.prettify())
        doc = open('data.html', 'r')
        soup2 = BeautifulSoup(doc, 'html.parser')


        filter_id = soup.find_all('div', class_='col dsk-span-12 item-box-hash')
        for id in filter_id:
            #print(id.text)
            clear_id = id.text.replace('item ID:', '')
            file.write(clear_id +'\n')
        filter_things = soup.find_all('div', class_="col dsk-span-9 tbt-span-8 mob-span-12 spec-data text-left text-bold text-em-5")
        for things in filter_things:
            #print(things.text)
            clear_things = things.text
            print(clear_things)
            file.write(str(filter_things) + '\n')

        # filter_price = soup.find_all('b', class_="text-em-5")
        # for price in filter_price:
        #     clear_price = price.text.replace('USD', '')
        #     #print(clear_price)
        #     file.write(str(filter_price) + '\n')
        #
        # filter_stock = soup.find_all('div', class_="text-status-green col-mt10 text-em-2")
        # for stock in filter_stock:
        #     #print(stock.text)
        #     file.write(str(filter_stock) + '\n')
        #
        # filter_not_in_stock = soup.find_all('span', class_="col-mr10 text-mid text-em-5")
        # for not_stock in filter_not_in_stock:
        #     #print(not_stock.text)
        #     file.write(str(filter_not_in_stock) + '\n')
        #
        # detail_type = soup.find_all('span', {'data-key': 'i27'})
        # for type in detail_type:
        #     #print(type.text)
        #     clear_detail_type = type.text
        #     file.write(str(detail_type) + '\n')
        #
        # detail_size = soup.find_all('span', {'data-key': 'i0'}, class_="filter-spec no-mob")
        # for size in detail_size:
        #     #print(size.text)
        #     clear_detail_size = size.text
        #     file.write(str(detail_size) + '\n')
        #
        # detail_hd = soup.find_all('span', {'data-key': 'i2'})
        # for hd in detail_hd:
        #     #print(hd.text)
        #     clear_detail_size = hd.text
        #     file.write(str(detail_hd) + '\n')
        #
        # detail_surface_type = soup.find_all('span', {'data-key': 'i3'})
        # for surface in detail_surface_type:
        #     #print(surface.text)
        #     clear_detail_surface_type = surface.text
        #     file.write(str(detail_surface_type) + '\n')
        #
        # detail_connector = soup.find_all('span', {'data-key': 'i23'})
        # for con in detail_connector:
        #     #print(con.text)
        #     clear_detail_connector = con.text
        #     file.write(str(detail_connector) + '\n')
        #
        # detail_fix = soup.find_all('span', {'data-key': 'i24'})
        # for fix in detail_fix:
        #     #print(fix.text)
        #     clear_detail_fix = fix.text
        #     file.write(str(detail_fix) + '\n')
        # #









