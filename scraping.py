
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
#from proxy import *
d = []
#proxies = {"http": "http://113.130.126.2:31932",
           #"https": "http://113.130.126.2:31932"}
import pandas as pd
print('Started WEB-Spider....')
with open('other.txt', 'r') as f:







    count =1

    for line in f:

        count +=1
        print('count is now -------->' + str(count))
        r_count = random.randrange(24, 32)
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
        # prox = {'http': proxies,
        #         'https': proxies
        # }
        get_html = requests.get(url, cookies=cookie, headers={"User-Agent": chr})
        #print(get_html)
        soup = BeautifulSoup(get_html.content, 'html5lib')

        f = furl.furl(url)
        clear_file = str(f.path).split('/')
        data_file = clear_file[3]
        d_file = clear_file[3]



        data_to_csv = open('/home/mirinda/Documents/update_pars/content/' + d_file +'.csv','a')






        detail_id =  soup.find_all('div', class_='col dsk-span-12 item-box-hash')
        if detail_id:
            for id in detail_id:
                clear_id = id.text.replace('item ID:', '')  # PRODUCT ID
        else:
            clear_id = ''


        detail_things = soup.find_all('div', 'col dsk-span-9 tbt-span-8 mob-span-12 spec-data text-left text-bold text-em-5')
        if detail_things:
            for things in detail_things:
                clear_things = things.text
        else:
            clear_things = ''










        filter_price = soup.find_all('b', class_="text-em-5") # PRODUCT PRICE
        if filter_price:
            for price in filter_price:
                clear_price = price.text.replace('USD', '')
                clear_prices = clear_price.split()
                clear_pric = ''.join(clear_prices)
        else:
            clear_pric = ''









        detail_type = soup.find_all('span', {'data-key': 'i27'})
        if detail_type:
            for type in detail_type:
                clear_detail_type = type.text
        else:
            clear_detail_type = ''

        detail_size = soup.find_all('span', {'data-key': 'i0'}, class_="filter-spec no-mob")
        if detail_size:
            for size in detail_size:
                clear_detail_size = size.text
        else:
            clear_detail_size = ''


        detail_hd = soup.find_all('span', {'data-key': 'i2'})
        if detail_hd:
            for hd in detail_hd:
                clear_hd = hd.text
        else:
            detail_hd = ''


        detail_surface_type = soup.find_all('span', {'data-key': 'i3'})
        if detail_surface_type:
            for surface in detail_surface_type:

                clear_detail_surface_type = surface.text
        else:
            clear_detail_surface_type = ''

        detail_connector = soup.find_all('span', {'data-key': 'i23'})
        if detail_connector:
            for con in detail_connector:

                clear_detail_connector = con.text
        else:
            clear_detail_connector = ''

        detail_fix = soup.find_all('span', {'data-key': 'i24'})
        if detail_fix:
            for fix in detail_fix:
                clear_detail_fix = fix.text
        else:
            clear_detail_fix = ''


        detail_serias = soup.find_all('div', class_="col dsk-span-9 tbt-span-8 mob-span-12 spec-data text-left text-bold text-em-5")
        for seria in detail_serias:
            if detail_serias:
                try:
                    for seria in detail_serias:
                        clear_detail_seria = seria.text
                        seria_list = clear_detail_seria.split()
                        clear_seria_list = seria_list[1]
                        print(clear_seria_list)
                except IndexError:
                    clear_seria_list = clear_detail_seria
                    print('IndexError!!!!!')
            else:
                clear_seria_list = ''
                print('Not Seria!!!!')









        detail_compatibility = soup.find_all('div', class_="col dsk-span-9 tbt-span-8 mob-span-12 spec-data text-left text-bold text-em-5")
        if detail_compatibility:
            for com in detail_compatibility:
                clear_detail_com = com.text
        else:
            clear_detail_com = ''

        detail_things_list = soup.find_all('div', class_="col dsk-span-9 tbt-span-8 mob-span-12 spec-data text-left text-bold text-em-5")
        if detail_things_list:
            try:
                for th in detail_things_list:
                    things_list = th.text
                    list_things = things_list.split()
                    clear_thing_list = list_things[2]
            except IndexError:
                clear_thing_list = things_list
        else:
            clear_thing_list = ''




        type_matrix = soup.find_all('span', {'data-key': 'i25'} , class_='filter-spec')
        if type_matrix:
            for matrix in type_matrix:
                type_mat = matrix.text
                print(type_mat)
        else:
            type_mat = ''
            print('Not Matrix!!!!!!!')







        type_grade = soup.find_all('span', {'data-key': ''}, class_='filter-spec')
        if type_grade:
            try:
                for grade in type_grade:
                    type_grd = grade.text
                    list_grd = type_grd.split()
                    clear_grd = list_grd[-1]
                    print(clear_grd)
            except IndexError:
                clear_grd = list_grd
                print('Index Error!!!!')
        else:
            clear_grd = ''
            print('Not Grade!!!!!!!')





        type_life = soup.find_all('span', {'data-key': ''}, class_='filter-spec')
        if type_life:
            try:
                for life in type_life:
                    type_lf = life.text
                    list_lf = type_lf.split()
                    clear_lf = list_lf[0]
            except IndexError:
                clear_lf = list_grd
                print('Not CLEAR_LF!!!')
        else:
            clear_lf = ''
            print(('NOY TYPE_LIFE!!!!'))




        type_url = soup.find_all('link', {'rel': 'alternate'}, {"hreflang": "en"}, href=True)
        if type_url:
            for ul in type_url:
                type_ul = ul.get('href')
        else:
            type_ul = ''

        error_404 = soup.find_all('title')
        if error_404:
            for er in error_404:
                error = er.text[0:3]
                if error == '404':
                    print(error)
                    question = input('Enter plz "y" and we continue:    ')
                    if question == 'y':
                        continue
                    else:
                        time.sleep(28800)
        else:
            continue



        d.append(())
        try:
            with open('/home/mirinda/Documents/update_pars/content/' + d_file + '.csv', 'a') as files:
                writer = csv.writer(files)
                writer.writerow([clear_id, clear_things, d_file, clear_seria_list, clear_thing_list, clear_things, clear_detail_com, clear_detail_type, clear_detail_size, clear_hd, clear_detail_surface_type, clear_detail_connector, clear_detail_fix, type_mat, clear_lf, clear_pric, type_ul])

        except:
            continue