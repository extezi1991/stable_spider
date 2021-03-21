from bs4 import BeautifulSoup, SoupStrainer
import requests
from fake_useragent import UserAgent
ua = UserAgent()
chr = ua.opera


doc_2_link = open('asus.txt', 'a')
doc_link = open('stage_2.txt', 'r')
f = open('stage_2.txt')
for line in f.readlines():
    line = line.rstrip('\n')
    # print(line)

    doc_2_link = open('asus.txt', 'a')
    #print (line),
    # line = f.readline()
    req = requests.get(line)
    cookie = req.cookies
    print(cookie)
    #print(line)
    get_html = requests.get(line, cookies=cookie, headers={"User-Agent": chr})
    print(get_html)
    soup = BeautifulSoup(get_html.content, 'html.parser')
    #print(line[0:-1])
    for link in soup.findAll("a", class_="brand-link link-no-decals block-inline", href=True):
        # print(link)
        doc_2_link.write("https://www.laptopscreen.com" + link.get('href') + '\n')
    for link in soup.findAll("a", class_="brand-link link-no-decals block-inline", href=True):
        # print(link)
        doc_2_link.write("https://www.laptopscreen.com" + link.get('href') + '?pgn&page=5' + '\n')

    for link in soup.findAll("a", class_="brand-link link-no-decals text-center", href=True):
        doc_2_link.write("https://www.laptopscreen.com" + link.get('href') + '\n')
            #doc_link.close()
        #?pgn&page=5
    for link in soup.findAll("a", class_="link-no-decals block brand-link brand-link-padded", href=True):
        doc_2_link.write("https://www.laptopscreen.com" + link.get('href') + '\n')

    doc_link.close()
    doc_2_link.close()
f.close()