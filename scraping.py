
from bs4 import BeautifulSoup, SoupStrainer
import requests
import csv
from fake_useragent import UserAgent
from saver import *
import furl
import time
import random
ua = UserAgent()
chr = ua.opera
d = []

import pandas as pd
print('Started WEB-Spider....')
with open('other.txt', 'r') as f:







    count =1

    for line in f:

        count +=1
        print('count is now -------->' + str(count))
        r_count = random.randrange(51, 60)
        r_sleep = random.randrange(21, 30)
        print('Stoping in -------->'+ str(r_count))
        print('Sleeping in -------->' + str(r_sleep))

        if count >= r_count:
            time.sleep(r_sleep)
            count = 0

        url = str(line.strip('\n'))

        print('---------------------------' + url)

        req = requests.get(str(line))
        cookie = req.cookies
        #print(cookie)
        #print(line)
        get_html = requests.get(url, cookies=cookie, headers={"User-Agent": chr})
        #print(get_html)
        soup = BeautifulSoup(get_html.content, 'html5lib')

        f = furl.furl(url)
        clear_file = str(f.path).split('/')
        data_file = clear_file[3]
        d_file = clear_file[3]



        data_to_csv = open('/home/mirinda/Documents/spider_now/content/' + d_file +'.csv','a')






        for id in soup.find_all('div', class_='col dsk-span-12 item-box-hash'):
            clear_id = id.text.replace('item ID:', '')  # PRODUCT ID


        for things in soup.find_all('div',class_="col dsk-span-9 tbt-span-8 mob-span-12 spec-data text-left text-bold text-em-5"):
            clear_things = things.text










        filter_price = soup.find_all('b', class_="text-em-5") # PRODUCT PRICE
        for price in filter_price:

            clear_price = price.text.replace('USD', '')
            clear_pric = '{:>12}'.format(clear_price)








        detail_type = soup.find_all('span', {'data-key': 'i27'})
        for type in detail_type:

            clear_detail_type = type.text


        detail_size = soup.find_all('span', {'data-key': 'i0'}, class_="filter-spec no-mob")
        for size in detail_size:

            clear_detail_size = size.text


        detail_hd = soup.find_all('span', {'data-key': 'i2'})
        for hd in detail_hd:

            clear_hd = hd.text


        detail_surface_type = soup.find_all('span', {'data-key': 'i3'})
        for surface in detail_surface_type:

            clear_detail_surface_type = surface.text


        detail_connector = soup.find_all('span', {'data-key': 'i23'})
        for con in detail_connector:

            clear_detail_connector = con.text


        detail_fix = soup.find_all('span', {'data-key': 'i24'})
        for fix in detail_fix:

            clear_detail_fix = fix.text


        detail_serias = soup.find_all('div', class_="col dsk-span-9 tbt-span-8 mob-span-12 spec-data text-left text-bold text-em-5")
        for seria in detail_serias:
            clear_detail_seria = seria.text
            seria_list = clear_detail_seria.split()

            try:
                clear_seria_list = seria_list[1]

            except:
                clear_seria_list = clear_detail_seria

        detail_compatibility = soup.find_all('div', class_="col dsk-span-9 tbt-span-8 mob-span-12 spec-data text-left text-bold text-em-5")
        for com in detail_compatibility:

            clear_detail_com = com.text

        detail_things_list = soup.find_all('div', class_="col dsk-span-9 tbt-span-8 mob-span-12 spec-data text-left text-bold text-em-5")
        for th in detail_things_list:
            things_list = th.text
            list_things = things_list.split()


            try:
                clear_thing_list = list_things[2]
            except:
                clear_thing_list = things_list


        type_matrix = soup.find_all('span', {'data-key': 'i25'} , class_='filter-spec')
        for matrix in type_matrix:

            type_mat = matrix.text

        type_grade = soup.find_all('span', {'data-key': ''}, class_='filter-spec')
        for grade in type_grade:

            type_grd = grade.text

            try:
                list_grd = type_grd.split()
                clear_grd = list_grd[-1]
            except:
                continue



        type_life = soup.find_all('span', {'data-key': ''}, class_='filter-spec')
        for life in type_life:

            type_lf = life.text

            try:
                list_lf = type_lf.split()
                clear_lf = list_lf[0]
            except:
                continue

        type_url = soup.find_all('link', {'rel': 'alternate'}, {"hreflang": "en"}, href=True)

        for ul in type_url:

            type_ul = ul.get('href')



        d.append(())
        try:
            with open('/home/mirinda/Documents/spider_now/content/' + d_file + '.csv', 'a') as files:
                writer = csv.writer(files)
                writer.writerow([clear_id, clear_things, d_file, clear_seria_list, clear_thing_list, clear_things, clear_detail_com, clear_detail_type, clear_detail_size, clear_hd, clear_detail_surface_type, clear_detail_connector, clear_detail_fix, type_mat, clear_lf, clear_pric, type_ul])

        except:
            continue