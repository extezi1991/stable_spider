from fake_useragent import UserAgent
ua = UserAgent()
chr = ua.opera
import requests
from bs4 import BeautifulSoup
import time
#from clock import *
cookies_file = open('/home/mirinda/Pycharm/rep_from_dev/cookie.txt', "r")
f = open('stage_2.txt', 'r')
while True:
    with open('/home/mirinda/Pycharm/rep_from_dev/cookie.txt', 'r') as f:
        cooks = f.read().splitlines()
        cooks = str(cooks)
    print(cooks)
    f = open('stage_2.txt', 'r')
    for line in f.readlines():
        page = 1
        for cook in cookies_file.readlines():
            cooks = str(cook)
            # print(cooks)

        req = requests.get(line)
        cookie = {"session": cooks}
        line = line.rstrip('\n')
        page = 1
        doc_2_link = open('apple.txt', 'a')
        main_url = (line + '?pgn&page=' + str(page))
        source_code = requests.get(main_url, cookies=cookie, headers={"User-Agent": chr}, verify = False)
        soup = BeautifulSoup(source_code.content, 'html.parser')
        doc_with_urls = open('apple.txt', 'a')
        # req = requests.get(main_url)
        cookie = {"session": cooks}
        for i in reversed(soup.findAll('a', title=True, class_='paginate')):
            num = i.text
            if num == i.text:
                num = int(num)
                print(num)
                break
        else:
            num = 1


        def find_url():
            page = 1




            while page <= num:
                with open('/home/mirinda/Pycharm/rep_from_dev/cookie.txt', 'r') as f:
                    cooks = f.read().splitlines()
                    cooks = str(cooks)
                print(cooks)


                # first_url = (line)
                main_url = (line + '?pgn&page=' + str(page))
                last_url = (line + '?pgn&page=' + str(num))
                req = requests.get(main_url)
                cookie = {"session": cooks}
                doc_with_urls = open('apple.txt', 'a')
                print(cookie)
                page += 1

                # first_code = requests.get(first_url, cookies=cookie, headers={"User-Agent": chr})
                source_code = requests.get(main_url, cookies=cookie, headers={"User-Agent": chr})
                last_code = requests.get(last_url, cookies=cookie, headers={"User-Agent": chr})
                # first_soup = BeautifulSoup(first_code.content, 'html.parser')
                soup = BeautifulSoup(source_code.content, 'html.parser')
                # last_soupe = BeautifulSoup(last_code.content, 'html.parser')
                status_url = source_code.status_code

                if status_url == 200:
                    last_num = num + 1

                    print('Status - Code = 200')

                    print(main_url)
                    for link in soup.findAll("a", class_="block brand-link link-no-decals", href=True):
                        doc_with_urls.write("https://www.laptopscreen.com" + link.get('href') + '\n')

                        if main_url == (line + '?pgn&page=' + str(last_num)):
                            doc_with_urls.write("https://www.laptopscreen.com" + link.get('href') + '\n')
                            break





                    else:

                        for link in soup.findAll("a", class_="brand-link link-no-decals block-inline",
                                                 href=True):
                            doc_with_urls.write("https://www.laptopscreen.com" + link.get('href') + '\n')

                            if main_url == (line + '?pgn&page=' + str(last_num)):
                                doc_with_urls.write("https://www.laptopscreen.com" + link.get('href') + '\n')
                                break
                        #time.sleep(5)


                else:
                    break


        find_url()









